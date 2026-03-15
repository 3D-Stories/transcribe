"""MCP server for audio transcription using AssemblyAI."""
import json
import os
import shutil
import subprocess
import time

import assemblyai as aai
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

# Load .env from server directory
_server_dir = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(_server_dir, ".env"))

# Cleanup stale temp dirs (older than 24h) on startup
_tmp_base = "/tmp/transcribe"
if os.path.exists(_tmp_base):
    now = time.time()
    for entry in os.listdir(_tmp_base):
        entry_path = os.path.join(_tmp_base, entry)
        if os.path.isdir(entry_path):
            age = now - os.path.getmtime(entry_path)
            if age > 86400:
                shutil.rmtree(entry_path, ignore_errors=True)

mcp = FastMCP("transcribe-mcp")


def _check_api_key() -> str | None:
    """Return API key or None if not configured."""
    key = os.environ.get("ASSEMBLYAI_API_KEY", "").strip()
    return key if key and key != "your_key_here" else None


def _convert_to_mp3(file_path: str) -> str:
    """Convert audio file to mp3 using ffmpeg. Returns path to mp3 file.

    The mp3 is written to the same directory as the input file.
    This ensures converted files go to the temp directory, not next to
    permanently stored files.
    """
    if file_path.lower().endswith(".mp3"):
        return file_path

    output_dir = os.path.dirname(file_path)
    basename = os.path.splitext(os.path.basename(file_path))[0]
    mp3_path = os.path.join(output_dir, basename + ".mp3")

    result = subprocess.run(
        ["ffmpeg", "-i", file_path, "-y", "-q:a", "2", mp3_path],
        capture_output=True, text=True, timeout=300
    )
    if result.returncode != 0:
        raise RuntimeError(f"ffmpeg conversion failed: {result.stderr[:500]}")
    return mp3_path


def _merge_consecutive_utterances(utterances: list[dict]) -> list[dict]:
    """Merge consecutive utterances from the same speaker."""
    if not utterances:
        return utterances

    merged = [utterances[0].copy()]
    for utt in utterances[1:]:
        if utt.get("speaker") == merged[-1].get("speaker"):
            merged[-1]["end_ms"] = utt["end_ms"]
            merged[-1]["text"] += " " + utt["text"]
            merged[-1]["confidence"] = round(
                (merged[-1]["confidence"] + utt["confidence"]) / 2, 3
            )
        else:
            merged.append(utt.copy())
    return merged


@mcp.tool()
def transcribe_audio(
    file_path: str,
    diarize: bool = True,
    language: str = "en",
) -> str:
    """Transcribe an audio file using AssemblyAI.

    Args:
        file_path: Path to audio file on this machine.
        diarize: Enable speaker diarization (default True).
        language: Language code or "auto" for detection (default "en").

    Returns:
        JSON string with utterances, duration, speakers detected, and status.
        On error, returns JSON with "error" and "message" fields.
    """
    # Check API key
    api_key = _check_api_key()
    if not api_key:
        return json.dumps({
            "error": "api_key_missing",
            "message": "AssemblyAI API key not configured in .env"
        })

    # Validate file exists
    if not os.path.isfile(file_path):
        return json.dumps({
            "error": "file_not_found",
            "message": f"File not found: {file_path}"
        })

    # Check disk space (need at least 500MB free in /tmp)
    stat = shutil.disk_usage("/tmp")
    if stat.free < 500 * 1024 * 1024:
        return json.dumps({
            "error": "disk_full",
            "message": f"Less than 500MB free on /tmp ({stat.free // (1024*1024)}MB available)"
        })

    try:
        # Convert to mp3 if needed
        mp3_path = _convert_to_mp3(file_path)

        # Configure AssemblyAI
        aai.settings.api_key = api_key

        config_kwargs = {"speech_models": ["universal-3-pro", "universal-2"]}
        if diarize:
            config_kwargs["speaker_labels"] = True
        if language == "auto":
            config_kwargs["language_detection"] = True
        else:
            config_kwargs["language_code"] = language

        config = aai.TranscriptionConfig(**config_kwargs)

        # Transcribe
        transcriber = aai.Transcriber()
        transcript = transcriber.transcribe(mp3_path, config)

        if transcript.status == aai.TranscriptStatus.error:
            return json.dumps({
                "error": "transcription_failed",
                "message": transcript.error or "Unknown transcription error"
            })

        # Build utterances from diarized output
        utterances = []
        if diarize and transcript.utterances:
            for utt in transcript.utterances:
                utterances.append({
                    "start_ms": utt.start,
                    "end_ms": utt.end,
                    "speaker": utt.speaker,
                    "text": utt.text,
                    "confidence": round(utt.confidence, 3) if utt.confidence else 0.0,
                })
        elif transcript.words:
            # No diarization — build utterances from words grouped by pauses.
            PAUSE_THRESHOLD_MS = 2000
            current = {"start_ms": 0, "end_ms": 0, "speaker": "A", "text": "", "confidence": 0.0}
            confs = []
            for word in transcript.words:
                if current["text"] and (word.start - current["end_ms"] > PAUSE_THRESHOLD_MS):
                    current["confidence"] = round(sum(confs) / len(confs), 3) if confs else 0.0
                    utterances.append(current)
                    current = {"start_ms": word.start, "end_ms": word.end, "speaker": "A", "text": word.text, "confidence": 0.0}
                    confs = [word.confidence] if word.confidence else []
                else:
                    if not current["text"]:
                        current["start_ms"] = word.start
                    current["end_ms"] = word.end
                    current["text"] = (current["text"] + " " + word.text).strip()
                    if word.confidence:
                        confs.append(word.confidence)
            if current["text"]:
                current["confidence"] = round(sum(confs) / len(confs), 3) if confs else 0.0
                utterances.append(current)

        # Merge consecutive same-speaker utterances
        utterances = _merge_consecutive_utterances(utterances)

        # Detect unique speakers
        speakers = set(u["speaker"] for u in utterances)

        # Calculate duration
        duration_ms = transcript.audio_duration
        duration_seconds = duration_ms // 1000 if duration_ms else 0

        result = {
            "utterances": utterances,
            "duration_seconds": duration_seconds,
            "speakers_detected": len(speakers),
            "language": transcript.language_code or language,
            "status": "completed",
        }

        result_json = json.dumps(result)

        # If result is too large (>8000 tokens ~= 32000 chars), write to file
        if len(result_json) > 32000:
            output_dir = os.path.dirname(file_path)
            output_path = os.path.join(output_dir, "transcript_result.json")
            with open(output_path, "w") as f:
                f.write(result_json)
            return json.dumps({
                "status": "completed_large",
                "result_file": output_path,
                "duration_seconds": duration_seconds,
                "speakers_detected": len(speakers),
                "utterance_count": len(utterances),
                "message": "Transcript too large for MCP response. Full result written to file."
            })

        return result_json

    except subprocess.TimeoutExpired:
        return json.dumps({
            "error": "ffmpeg_timeout",
            "message": "Audio conversion timed out after 5 minutes"
        })
    except Exception as e:
        return json.dumps({
            "error": "unexpected_error",
            "message": str(e)[:500]
        })


if __name__ == "__main__":
    mcp.run()

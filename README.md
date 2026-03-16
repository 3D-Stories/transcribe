# transcribe

A Claude Code plugin that transcribes audio and video files into organized markdown documents with speaker diarization.

## Features

- Transcribes any audio format (m4a, mp3, wav, ogg, flac, etc.)
- Transcribes any video format (mp4, mkv, mov, avi, webm, etc.) — extracts audio automatically
- Speaker diarization (identifies who said what)
- Three output formats: Summary + Transcript, Summary only, or Transcript only
- Guided first-time setup — walks you through installing ffmpeg, setting up the transcription server, and getting an AssemblyAI API key
- Supports local or remote (SSH) server deployment

## Installation

```bash
claude plugin install 3D-Stories/transcribe
```

## Usage

```
/transcribe path/to/recording.mp4
/transcribe meeting-notes.m4a
```

On first run, the skill walks you through setup:
1. Checks for ffmpeg
2. Asks where to install the transcription server (local or remote)
3. Creates the server with AssemblyAI integration
4. Guides you through getting an API key
5. Saves config for future runs

## Output

Transcripts are written to a `transcripts/` directory in your project:

- `transcripts/<filename>_summary.md` — structured summary with key decisions, action items, and timeline
- `transcripts/<filename>_transcription.md` — full speaker-labeled transcript with timestamps

## How It Works

The plugin bundles a Python MCP server that wraps the AssemblyAI API. On each transcription:

1. Video files have audio extracted via ffmpeg (codec copy for speed)
2. Audio is transferred to the server host (local or via SCP)
3. AssemblyAI transcribes with speaker diarization
4. Results are structured into markdown with summaries and timestamps
5. Temp files are cleaned up

## Configuration

After first-time setup, config is stored at `.transcribe-config.json` in your project root:

```json
{
  "mcp_host": "user@server",
  "mcp_path": "/opt/mcp-servers/transcribe-mcp",
  "remote": true
}
```

This file is gitignored since it contains host-specific details.

## Cost

AssemblyAI charges $0.0065 per minute of audio (~$0.39/hour). The skill shows you the estimated cost before each transcription and asks for approval.

## License

MIT

---
description: Transcribe an audio or video file into an organized markdown document with speaker diarization. Accepts any audio format (m4a, mp3, wav, ogg, flac, etc.) and any video format (mp4, mkv, mov, avi, webm, etc.) — video files have their audio extracted automatically before transcription. Includes guided first-time setup for the transcription server, ffmpeg, and AssemblyAI API key. Use this skill whenever the user mentions transcribing, transcription, speech-to-text, converting audio/video to text, or wants a written record of a recording.
---

# Audio & Video Transcription Skill

You are orchestrating the transcription of an audio or video file into an organized markdown document. Video files are handled transparently — the audio track is extracted first, then transcribed like any audio file.

The transcription server can run locally or on a remote host via SSH. Configuration is stored in `.transcribe-config.json` in the project root (this keeps host-specific settings outside the plugin cache, which gets recreated on plugin updates). If no config exists, the skill walks the user through first-time setup.

## Arguments

The user provides a path to an audio or video file as: $ARGUMENTS
If no arguments were provided, ask the user for the file path.

## Step 0: Prerequisites Check

Check for the config file at `.transcribe-config.json` in the project root (the current working directory).

**If the config file does not exist:** This is a first-time run. Read `references/setup-guide.md` (in this skill's directory) and follow the setup walkthrough with the user. Once setup is complete and config.json is written, return here and proceed to Step 1.

**If the config file exists:** Read it and remember the values for subsequent steps:
- `mcp_host` — SSH connection string (e.g., `root@10.0.17.204`) or `null` for local
- `mcp_path` — installation path of the transcription server
- `remote` — `true` if the server is on a remote host, `false` if local

Proceed to Step 1.

Throughout the rest of this skill, `<mcp_host>`, `<mcp_path>`, and `<remote>` refer to these config values. Commands that run on the server host should be:
- **If remote:** wrapped in `ssh <mcp_host> "..."`
- **If local:** run directly without SSH

## Step 1: Validate Media File

Check that the file at the given path exists using the Bash tool:

```
test -f "$ARGUMENTS" && echo "EXISTS" || echo "NOT FOUND"
```

If the file does not exist, try resolving it relative to the current working directory. If still not found, inform the user and stop.

## Step 1b: Detect Video & Extract Audio

Check whether the file contains a video stream using ffprobe:

```bash
ffprobe -v quiet -select_streams v -show_entries stream=codec_type -of csv=p=0 "<file_path>"
```

- **If the output contains `video`** → this is a video file. Extract the audio:
  ```bash
  ffmpeg -i "<file_path>" -vn -acodec copy "/tmp/transcribe_extracted_$(basename "<file_path>" | sed 's/\.[^.]*$//').m4a" -y 2>&1
  ```
  If the copy fails (incompatible codec/container), fall back to re-encoding:
  ```bash
  ffmpeg -i "<file_path>" -vn -acodec aac -b:a 128k "/tmp/transcribe_extracted_$(basename "<file_path>" | sed 's/\.[^.]*$//').m4a" -y 2>&1
  ```
  Update the working file path to the extracted audio for all subsequent steps. Remember the original filename for output naming.

- **If no video stream** → the file is audio-only. Continue with the original file path.

**If ffprobe or ffmpeg is not found:** Tell the user ffmpeg is not installed and offer to run setup. Read `references/setup-guide.md` starting from Step S1.

## Step 2: Probe Duration and Estimate Cost

Get the audio duration using ffprobe (use the working file path — either the original audio or the extracted audio):

```
ffprobe -v quiet -show_entries format=duration -of csv=p=0 "<working_file_path>"
```

Calculate:

- Duration in minutes and seconds
- Estimated cost: `duration_minutes x $0.0065` (AssemblyAI pricing)
- Estimated processing time: ~5 minutes for 1 hour of audio

## Step 3: Ask User Approval

Present this information to the user using AskUserQuestion with **two questions**:

**Question 1 — Approval:**

```
Audio: <filename> (<duration>)
Estimated cost: $<cost> (AssemblyAI @ $0.0065/min)
Estimated time: ~<estimate>

Proceed with transcription?
```

Options: "Proceed" / "Cancel"

If the user cancels, stop.

**Question 2 — Output format:**

```
What output format would you like?
```

Options:

- "Summary + Transcript" — structured summary with key points, followed by the full transcript
- "Summary only" — structured summary with key points, timestamps, and quotes (no full transcript)
- "Transcript only" — raw full transcript with speaker labels and timestamps (no analysis)

Remember the user's choice for Step 7.

## Step 4: Transfer Audio to Server

Generate a UUID for the temp directory and transfer the working file to the server host:

### If remote:

```bash
UUID=$(python3 -c "import uuid; print(uuid.uuid4().hex[:12])")
ssh <mcp_host> "mkdir -p /tmp/transcribe/${UUID}"
scp "<working_file_path>" "<mcp_host>:/tmp/transcribe/${UUID}/"
```

### If local:

```bash
UUID=$(python3 -c "import uuid; print(uuid.uuid4().hex[:12])")
mkdir -p /tmp/transcribe/${UUID}
cp "<working_file_path>" "/tmp/transcribe/${UUID}/"
```

Remember the server-side path: `/tmp/transcribe/<UUID>/<filename>`

**If SSH/SCP fails:** The server may be unreachable. Tell the user and offer to re-check the setup. Read `references/setup-guide.md` for troubleshooting guidance.

## Step 5: Run Transcription

Try two approaches in order:

### Approach A: MCP Tool

Use ToolSearch to find `transcribe_audio`. If found, call it with:
- `file_path`: the server-side path from Step 4
- `diarize`: true
- `language`: "en"

### Approach B: Direct Python invocation (fallback)

If the MCP tool is not available in this session, call the transcription function directly on the server host:

```bash
# Remote:
ssh <mcp_host> "cd <mcp_path> && .venv/bin/python3 -c \"
import sys, json
sys.path.insert(0, '.')
from server import transcribe_audio
result = transcribe_audio('/tmp/transcribe/<UUID>/<filename>', diarize=True, language='en')
print(result)
\""

# Local:
cd <mcp_path> && .venv/bin/python3 -c "
import sys, json
sys.path.insert(0, '.')
from server import transcribe_audio
result = transcribe_audio('/tmp/transcribe/<UUID>/<filename>', diarize=True, language='en')
print(result)
"
```

Use a generous timeout (10 minutes) — transcription of long files can take several minutes.

## Step 6: Handle Response

Parse the JSON response from the transcription function.

**If `"error": "api_key_missing"`:**

1. Ask the user: "No AssemblyAI API key configured. Please paste your AssemblyAI API key:"
2. Store it on the server host using Python (to avoid shell injection):
   ```bash
   # Remote:
   ssh <mcp_host> "python3 -c \"
   import os
   with open('<mcp_path>/.env', 'w') as f:
       f.write('ASSEMBLYAI_API_KEY=<key>\n')
   os.chmod('<mcp_path>/.env', 0o600)
   \""

   # Local: same command without ssh wrapper
   ```
3. Retry the transcription (Step 5).

**If `"status": "completed_large"`:**

The result was too large for inline response and was written to a file. Read it:
```bash
# Remote:
ssh <mcp_host> "cat <result_file_path>"

# Local:
cat <result_file_path>
```
Parse the JSON and continue to Step 7.

**If any other `"error"`:**

1. Report the error to the user.
2. If the error suggests a setup issue (module not found, connection refused, file not found on server), offer to re-run setup by reading `references/setup-guide.md`.
3. Clean up temp files (Step 8) and stop.

**If `"status": "completed"`:**
Continue to Step 7.

## Step 7: Structure into Markdown

You now have the transcript as utterances with speaker labels. Create the markdown document based on the user's output format choice from Step 3.

**All documents start with a metadata header:**

```markdown
# <Title derived from filename>

**Source:** <filename>
**Duration:** <duration>
**Speakers:** <count> (<speaker labels>)
**Confidence:** <confidence>%
**Language:** <language>
```

---

### If "Summary + Transcript":

Include both the summary sections AND the full transcript at the end.

**Summary section** — choose the best headings based on what's actually in the recording. Select from these candidates (drop ones that don't apply, add better-fitting ones):

- **Summary** — always include, 2-4 paragraph high-level overview
- **Key Decisions** — if decisions were made during the conversation
- **Ideas & Concepts** — creative content, proposals, brainstorms
- **Action Items** — specific next steps or tasks mentioned
- **Discussion Points** — notable topics or exchanges
- **Questions Raised** — unresolved questions from the conversation
- **Participants** — speaker breakdown (Speaker A, B, etc.) with approximate talk time
- **Timeline** — chronological flow with timestamps for major topic changes

**Full Transcript section** — after the summary, include a `## Full Transcript` section with the complete text, speaker labels, and timestamps.

### If "Summary only":

Include only the summary sections listed above. Do NOT include the full transcript text.

### If "Transcript only":

Skip all analysis. Write only the metadata header followed by a `## Transcript` section containing the full text organized by speaker turns with `[MM:SS]` timestamps.

---

**Formatting rules (apply to all formats):**

- Include timestamps in `[MM:SS]` format for key moments
- Use speaker labels (Speaker A, Speaker B) consistently
- Use bullet points for lists, not numbered lists
- Keep the Summary concise but comprehensive (when included)
- Include direct quotes for important statements using blockquotes (when summary is included)

**Output file naming** — based on the format choice, use the appropriate suffix:

- **Summary + Transcript:** write TWO files:
  - `transcripts/<basename>_summary.md` (summary sections only)
  - `transcripts/<basename>_transcription.md` (full transcript only)
- **Summary only:** `transcripts/<basename>_summary.md`
- **Transcript only:** `transcripts/<basename>_transcription.md`

Where `<basename>` is the original filename without its extension.

If the `transcripts/` directory doesn't exist, create it:

```bash
mkdir -p transcripts
```

If a file with that name already exists, append a timestamp:
`<basename>_summary_YYYYMMDD-HHMMSS.md` or `<basename>_transcription_YYYYMMDD-HHMMSS.md`

## Step 8: Clean Up

Remove temp files from the server host:

```bash
# Remote:
ssh <mcp_host> "rm -rf /tmp/transcribe/<UUID>"

# Local:
rm -rf /tmp/transcribe/<UUID>
```

If audio was extracted from a video file in Step 1b, also remove the local temp file:

```bash
rm -f "/tmp/transcribe_extracted_<basename>.m4a"
```

## Step 9: Report to User

Tell the user:

- Which file(s) were written (e.g. `transcripts/<basename>_summary.md`, `transcripts/<basename>_transcription.md`, or both)
- How many speakers were detected
- The duration of the recording
- Offer to read or summarize the transcript

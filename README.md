# transcribe

A Claude Code plugin that transcribes audio and video files into organized markdown documents with speaker diarization.

## Features

- Transcribes any audio format (m4a, mp3, wav, ogg, flac, etc.)
- Transcribes any video format (mp4, mkv, mov, avi, webm, etc.) — extracts audio automatically
- Speaker diarization (identifies who said what)
- Three output formats: Summary + Transcript, Summary only, or Transcript only
- Guided first-time setup — walks you through everything below
- Supports local or remote (SSH) server deployment

## Prerequisites

### On your local machine (where Claude Code runs)

| Dependency | Purpose | Install |
|------------|---------|---------|
| **Claude Code** | Plugin host | [claude.com/claude-code](https://claude.com/claude-code) |
| **ffmpeg / ffprobe** | Video-to-audio extraction, duration probing | `sudo apt install ffmpeg` (Debian/Ubuntu) or `brew install ffmpeg` (macOS) |
| **Python 3.8+** | Only needed if running the MCP server locally | `sudo apt install python3 python3-venv` |
| **SSH client** | Only needed if the MCP server is on a remote host | Pre-installed on most systems |

### On the MCP server host (local or remote)

| Dependency | Purpose | Install |
|------------|---------|---------|
| **Python 3.8+** | Runs the transcription server | `sudo apt install python3 python3-venv python3-pip` |
| **ffmpeg** | Converts audio to MP3 before uploading to AssemblyAI | `sudo apt install ffmpeg` |
| **AssemblyAI API key** | Speech-to-text engine | Free account at [assemblyai.com](https://www.assemblyai.com) |

## Installation

```bash
claude plugin install 3D-Stories/transcribe
```

## Usage

```
/transcribe path/to/recording.mp4
/transcribe meeting-notes.m4a
```

On first run, the skill walks you through setup (see [Architecture](#architecture) for what gets installed where).

## Output

Transcripts are written to a `transcripts/` directory in your project:

- `transcripts/<filename>_summary.md` — structured summary with key decisions, action items, and timeline
- `transcripts/<filename>_transcription.md` — full speaker-labeled transcript with timestamps

## Architecture

The plugin has two parts: the **skill** (runs inside Claude Code) and the **MCP server** (runs on a host you choose).

```
┌─────────────────────────────────────────────────────────┐
│  Your machine (Claude Code)                             │
│                                                         │
│  /transcribe skill                                      │
│    ├── Validates input file                             │
│    ├── Extracts audio from video (ffmpeg)               │
│    ├── Estimates cost, asks for approval                │
│    ├── Transfers audio to MCP server host (SCP or cp)   │
│    ├── Calls transcribe_audio() on the server           │
│    └── Structures results into markdown                 │
│                                                         │
│  .transcribe-config.json  ← points to the server       │
└──────────────────────┬──────────────────────────────────┘
                       │ SCP + SSH (or local if same machine)
┌──────────────────────▼──────────────────────────────────┐
│  MCP Server Host (local or remote)                      │
│                                                         │
│  <install_path>/          e.g. /opt/mcp-servers/        │
│  └── transcribe-mcp/          transcribe-mcp/           │
│      ├── server.py        ← FastMCP server wrapping     │
│      │                       AssemblyAI API             │
│      ├── .venv/           ← Python virtualenv with      │
│      │                       assemblyai, python-dotenv, │
│      │                       mcp packages               │
│      ├── .env             ← ASSEMBLYAI_API_KEY=...      │
│      │                       (chmod 600)                │
│      └── requirements.txt                               │
└─────────────────────────────────────────────────────────┘
```

### What gets installed where

| Component | Location | Created by | Persists across |
|-----------|----------|------------|-----------------|
| **Plugin skill files** | `~/.claude/plugins/cache/...` | `claude plugin install` | Plugin reinstall recreates |
| **Project config** | `.transcribe-config.json` (project root) | First-time setup | Plugin updates, git clone |
| **MCP server** | `<install_path>/transcribe-mcp/` on chosen host | First-time setup | Everything (it's standalone) |
| **API key** | `<install_path>/transcribe-mcp/.env` on server host | First-time setup | Everything (it's on the server) |
| **Transcripts** | `transcripts/` (project root) | Each `/transcribe` run | Everything (your output) |

### First-time setup flow

When you first run `/transcribe`, the skill detects no `.transcribe-config.json` and walks you through:

1. **Checks ffmpeg** is installed locally
2. **Asks server location** — "This machine" or "A remote server via SSH"
3. **Copies `server.py` and `requirements.txt`** to the chosen host (bundled with the plugin)
4. **Creates a Python virtualenv** and installs dependencies (`assemblyai`, `python-dotenv`, `mcp`)
5. **Checks ffmpeg** on the server host (needed for audio format conversion)
6. **Guides you to get an AssemblyAI API key** — create account at [assemblyai.com](https://www.assemblyai.com), copy key from dashboard
7. **Stores the API key** in `<install_path>/transcribe-mcp/.env` (chmod 600)
8. **Writes `.transcribe-config.json`** to your project root

After setup, subsequent runs skip straight to transcription.

## How It Works

On each transcription:

1. Video files have audio extracted via ffmpeg (codec copy for speed, AAC re-encode as fallback)
2. Audio is transferred to the MCP server host (local `cp` or remote `scp`)
3. The server converts to MP3, uploads to AssemblyAI with speaker diarization enabled
4. AssemblyAI returns timestamped utterances with speaker labels and confidence scores
5. Claude structures the results into markdown (summary, transcript, or both)
6. Temp files are cleaned up on both local and server

## Configuration

After first-time setup, config is stored at `.transcribe-config.json` in your project root:

```json
{
  "mcp_host": "user@server",
  "mcp_path": "/opt/mcp-servers/transcribe-mcp",
  "remote": true
}
```

| Field | Description |
|-------|-------------|
| `mcp_host` | SSH connection string for remote server, or `null` for local |
| `mcp_path` | Absolute path to the `transcribe-mcp/` directory on the server host |
| `remote` | `true` if server is on a different machine, `false` if local |

This file is gitignored since it contains host-specific details. Each team member creates their own during first-time setup.

## Cost

AssemblyAI charges $0.0065 per minute of audio (~$0.39/hour). The skill shows you the estimated cost before each transcription and asks for approval.

## License

MIT

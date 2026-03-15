# Transcription Skill — First-Time Setup

This guide walks you through setting up everything needed for the `/transcribe` skill:
- ffmpeg (audio/video processing)
- A transcription server running the AssemblyAI-powered Python service
- An AssemblyAI API key

Work through these steps in order with the user.

---

## S1: Check Local Dependencies

### ffmpeg / ffprobe

```bash
which ffmpeg && ffmpeg -version | head -1
```

If not installed, tell the user:
- **Debian/Ubuntu:** `sudo apt install ffmpeg`
- **macOS:** `brew install ffmpeg`
- **Arch:** `sudo pacman -S ffmpeg`
- **Other:** Download from https://ffmpeg.org/download.html

ffmpeg is needed locally for video-to-audio extraction (Step 1b of the main skill) and on the server host for format conversion before upload to AssemblyAI.

### Python 3

```bash
python3 --version
```

If not installed:
- **Debian/Ubuntu:** `sudo apt install python3 python3-venv python3-pip`
- **macOS:** `brew install python3`

---

## S2: Get an AssemblyAI API Key

AssemblyAI provides the speech-to-text engine. Their pricing is $0.0065 per minute of audio (~$0.39/hour).

Walk the user through this:

1. Go to **https://www.assemblyai.com** and create a free account
2. After signing in, the API key is displayed on the **Dashboard** main page
3. If not visible, check **Settings > API Keys**
4. Copy the key — it will be needed in Step S5

Tell the user to keep the key handy (in their clipboard or a text file) until we store it securely on the server.

---

## S3: Choose Where to Install the Transcription Server

Ask the user using AskUserQuestion:

**"Where should the transcription server be installed?"**

Options:
- **"This machine (localhost)"** — Simplest setup. No SSH needed. Good for most users. The transcription processing (format conversion, API upload) happens on your local machine.
- **"A remote server via SSH"** — Install on a separate server (homelab VM, cloud instance, etc). Keeps heavy processing off your dev machine. Requires SSH key-based access to the remote host.

### If the user chooses remote:

Ask for the SSH connection string using AskUserQuestion:
- **"What's the SSH connection string for the server? (e.g., root@10.0.17.204 or user@my-server.local)"**

Then verify SSH connectivity:
```bash
ssh <host> "echo CONNECTION_OK"
```

If this fails, help set up SSH key-based auth:
1. Check for existing key: `ls ~/.ssh/id_ed25519.pub ~/.ssh/id_rsa.pub 2>/dev/null`
2. Generate if needed: `ssh-keygen -t ed25519`
3. Copy to remote: `ssh-copy-id <host>`
4. Test again: `ssh <host> "echo CONNECTION_OK"`

### Installation path

Ask the user using AskUserQuestion or suggest the default:
- **Remote server:** `/opt/mcp-servers/transcribe-mcp` (recommended)
- **Localhost:** `~/.local/share/transcribe-mcp` (recommended)

The user can provide any path they prefer.

---

## S4: Create the Transcription Server

The server source and dependencies are bundled with this skill at:
- `references/server.py`
- `references/requirements.txt`

The `<skill_dir>` is the directory containing this skill's SKILL.md file.

### Remote installation:

```bash
ssh <host> "mkdir -p <path>"
scp <skill_dir>/references/server.py <host>:<path>/server.py
scp <skill_dir>/references/requirements.txt <host>:<path>/requirements.txt
ssh <host> "cd <path> && python3 -m venv .venv && .venv/bin/pip install -r requirements.txt"
```

### Local installation:

```bash
mkdir -p <path>
cp <skill_dir>/references/server.py <path>/server.py
cp <skill_dir>/references/requirements.txt <path>/requirements.txt
cd <path> && python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
```

### Verify Python dependencies:

```bash
# Remote:
ssh <host> "cd <path> && .venv/bin/python3 -c 'import assemblyai; print(\"assemblyai OK\")'"

# Local:
cd <path> && .venv/bin/python3 -c "import assemblyai; print('assemblyai OK')"
```

### Verify ffmpeg on the server host

The server converts audio to MP3 before uploading to AssemblyAI, so ffmpeg must also be installed on the server host (which may be different from the local machine):

```bash
# Remote:
ssh <host> "which ffmpeg && echo FFMPEG_OK"

# Local:
which ffmpeg && echo FFMPEG_OK
```

If missing on the remote host, install it there using the same instructions from Step S1.

---

## S5: Store the API Key

Store the AssemblyAI API key securely on the server host. Use Python to write the file to avoid shell injection issues with special characters in the key.

### Remote:

```bash
ssh <host> "python3 -c \"
import os
with open('<path>/.env', 'w') as f:
    f.write('ASSEMBLYAI_API_KEY=<key>\n')
os.chmod('<path>/.env', 0o600)
\""
```

### Local:

```bash
python3 -c "
import os
with open('<path>/.env', 'w') as f:
    f.write('ASSEMBLYAI_API_KEY=<key>\n')
os.chmod('<path>/.env', 0o600)
"
```

Replace `<key>` with the actual API key from Step S2.

---

## S6: Save Configuration

Write the configuration file so the skill knows where the server lives on subsequent runs.

Write to `.claude/skills/transcribe/config.json`:

```json
{
  "mcp_host": "<user@host>",
  "mcp_path": "<installation path>",
  "remote": true
}
```

- If local installation, set `"mcp_host": null` and `"remote": false`
- If remote, `mcp_host` is the SSH connection string (e.g., `"root@10.0.17.204"`)

This file contains host-specific information. If the `.claude/` directory is tracked in git, add this to `.gitignore`:

```
.claude/skills/transcribe/config.json
```

---

## S7: Verification

Run a final check to confirm everything works end-to-end:

```bash
# Remote:
ssh <host> "cd <path> && .venv/bin/python3 -c \"
from dotenv import load_dotenv
load_dotenv('.env')
import os
key = os.environ.get('ASSEMBLYAI_API_KEY', '')
print('API key:', 'configured' if key and key != 'your_key_here' else 'MISSING')
\""

# Local:
cd <path> && .venv/bin/python3 -c "
from dotenv import load_dotenv
load_dotenv('.env')
import os
key = os.environ.get('ASSEMBLYAI_API_KEY', '')
print('API key:', 'configured' if key and key != 'your_key_here' else 'MISSING')
"
```

Tell the user: **"Setup complete! Run `/transcribe <audio-or-video-file>` to transcribe your first file."**

---

## Troubleshooting

### SSH connection refused
- Verify the host is reachable: `ping <host>`
- Check SSH service is running on the remote: `ssh <host> "systemctl status sshd"`
- Ensure your SSH key is authorized: `ssh-copy-id <host>`

### pip install fails
- Ensure Python 3.8+ is installed: `python3 --version`
- Try upgrading pip first: `.venv/bin/pip install --upgrade pip`
- If behind a proxy, set `HTTPS_PROXY` before pip install

### "No module named 'assemblyai'" at runtime
- The server must be invoked with the venv Python, not the system Python
- Verify: `<path>/.venv/bin/python3 -c "import assemblyai"`

### API key errors
- Verify the key at https://www.assemblyai.com/app (Dashboard)
- Check the .env file: `cat <path>/.env` (should show `ASSEMBLYAI_API_KEY=...`)
- Ensure the .env file is in the same directory as server.py

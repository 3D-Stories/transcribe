# transcribe — Plugin Development Instructions

## Versioning

This plugin uses semver in `.claude-plugin/plugin.json`:
- **patch** (1.0.x): bug fixes, doc typos, test additions
- **minor** (1.x.0): new features, new output formats, new setup options
- **major** (x.0.0): breaking changes to config format, skill interface, or server API

Keep `marketplace.json` version in sync with `plugin.json`.

## Pre-PR Checklist

Every PR must:
1. Bump version in `.claude-plugin/plugin.json`
2. Update `README.md` if user-facing behavior changes
3. Pass `pytest tests/ -v`
4. Update `references/setup-guide.md` if setup flow changes

## Git Workflow

- Never push directly to `main` — always use PRs
- Branch naming: `feature/<issue>-<description>` or `fix/<issue>-<description>`
- Squash merge PRs

## Project Structure

```
.claude-plugin/
  plugin.json          ← manifest (version lives here)
  marketplace.json     ← marketplace publishing metadata
skills/transcribe/
  SKILL.md             ← the skill prompt (Claude reads this)
  references/
    setup-guide.md     ← first-time setup walkthrough
    server.py          ← bundled MCP server source
    requirements.txt   ← Python deps for the MCP server
tests/
  test_plugin_structure.py  ← structural + workflow tests
```

## Testing

```bash
pytest tests/ -v
```

Tests validate plugin structure, skill content, and reference file integrity. They do not call AssemblyAI or require network access.

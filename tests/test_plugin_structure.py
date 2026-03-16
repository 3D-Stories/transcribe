"""Tests for the transcribe plugin structure and skill integrity."""
import json
import os
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).parent.parent


class TestPluginManifest:
    """Validate plugin.json meets Claude Code plugin requirements."""

    def test_manifest_exists(self):
        manifest = REPO_ROOT / ".claude-plugin" / "plugin.json"
        assert manifest.exists(), "Missing .claude-plugin/plugin.json"

    def test_manifest_valid_json(self):
        manifest = REPO_ROOT / ".claude-plugin" / "plugin.json"
        with open(manifest) as f:
            data = json.load(f)
        assert isinstance(data, dict)

    def test_manifest_has_name(self):
        with open(REPO_ROOT / ".claude-plugin" / "plugin.json") as f:
            data = json.load(f)
        assert "name" in data, "plugin.json must have 'name' field"
        assert data["name"] == "transcribe"

    def test_manifest_has_version(self):
        with open(REPO_ROOT / ".claude-plugin" / "plugin.json") as f:
            data = json.load(f)
        assert "version" in data
        parts = data["version"].split(".")
        assert len(parts) == 3, f"Version must be semver: {data['version']}"

    def test_manifest_has_description(self):
        with open(REPO_ROOT / ".claude-plugin" / "plugin.json") as f:
            data = json.load(f)
        assert "description" in data
        assert len(data["description"]) > 20, "Description should be substantive"


class TestSkillStructure:
    """Validate skill directory layout and SKILL.md content."""

    def test_skill_directory_exists(self):
        skill_dir = REPO_ROOT / "skills" / "transcribe"
        assert skill_dir.is_dir(), "Missing skills/transcribe/"

    def test_skill_md_exists(self):
        skill_md = REPO_ROOT / "skills" / "transcribe" / "SKILL.md"
        assert skill_md.exists(), "Missing skills/transcribe/SKILL.md"

    def test_skill_has_frontmatter(self):
        skill_md = REPO_ROOT / "skills" / "transcribe" / "SKILL.md"
        content = skill_md.read_text()
        assert content.startswith("---"), "SKILL.md must start with YAML frontmatter"
        # Find closing frontmatter delimiter
        second_dash = content.index("---", 3)
        assert second_dash > 3, "SKILL.md frontmatter must have closing ---"

    def test_skill_frontmatter_has_description(self):
        skill_md = REPO_ROOT / "skills" / "transcribe" / "SKILL.md"
        content = skill_md.read_text()
        frontmatter = content.split("---")[1]
        assert "description:" in frontmatter, "Frontmatter must include description"

    def test_skill_has_arguments_section(self):
        content = (REPO_ROOT / "skills" / "transcribe" / "SKILL.md").read_text()
        assert "## Arguments" in content

    def test_skill_has_prerequisites_check(self):
        content = (REPO_ROOT / "skills" / "transcribe" / "SKILL.md").read_text()
        assert "## Step 0: Prerequisites Check" in content

    def test_skill_references_config_in_project_root(self):
        """Config must be in project root, not inside the plugin cache."""
        content = (REPO_ROOT / "skills" / "transcribe" / "SKILL.md").read_text()
        assert ".transcribe-config.json" in content
        assert ".claude/skills/transcribe/config.json" not in content, \
            "Config path must not reference old .claude/skills/ location"


class TestReferences:
    """Validate bundled reference files."""

    def test_setup_guide_exists(self):
        f = REPO_ROOT / "skills" / "transcribe" / "references" / "setup-guide.md"
        assert f.exists()

    def test_server_py_exists(self):
        f = REPO_ROOT / "skills" / "transcribe" / "references" / "server.py"
        assert f.exists()

    def test_requirements_txt_exists(self):
        f = REPO_ROOT / "skills" / "transcribe" / "references" / "requirements.txt"
        assert f.exists()

    def test_server_has_transcribe_function(self):
        content = (REPO_ROOT / "skills" / "transcribe" / "references" / "server.py").read_text()
        assert "def transcribe_audio(" in content

    def test_server_has_mcp_decorator(self):
        content = (REPO_ROOT / "skills" / "transcribe" / "references" / "server.py").read_text()
        assert "@mcp.tool()" in content

    def test_requirements_has_assemblyai(self):
        content = (REPO_ROOT / "skills" / "transcribe" / "references" / "requirements.txt").read_text()
        assert "assemblyai" in content

    def test_setup_guide_references_correct_config_path(self):
        content = (REPO_ROOT / "skills" / "transcribe" / "references" / "setup-guide.md").read_text()
        assert ".transcribe-config.json" in content
        assert ".claude/skills/transcribe/config.json" not in content, \
            "Setup guide must not reference old config path"


class TestMarketplace:
    """Validate marketplace.json for plugin distribution."""

    def test_marketplace_exists(self):
        f = REPO_ROOT / ".claude-plugin" / "marketplace.json"
        assert f.exists(), "Missing .claude-plugin/marketplace.json"

    def test_marketplace_valid_json(self):
        with open(REPO_ROOT / ".claude-plugin" / "marketplace.json") as f:
            data = json.load(f)
        assert isinstance(data, dict)

    def test_marketplace_has_required_fields(self):
        with open(REPO_ROOT / ".claude-plugin" / "marketplace.json") as f:
            data = json.load(f)
        assert "name" in data
        assert "description" in data
        assert "owner" in data
        assert "plugins" in data

    def test_marketplace_owner_has_name(self):
        with open(REPO_ROOT / ".claude-plugin" / "marketplace.json") as f:
            data = json.load(f)
        assert "name" in data["owner"]

    def test_marketplace_plugin_has_source(self):
        """Plugin entry must use 'source' not 'path' — Claude Code validates this."""
        with open(REPO_ROOT / ".claude-plugin" / "marketplace.json") as f:
            data = json.load(f)
        plugin = data["plugins"][0]
        assert "source" in plugin, "Plugin entry must have 'source' field (not 'path')"
        assert "version" in plugin, "Plugin entry must have 'version' field"


class TestVersioning:
    """Validate version consistency across plugin files."""

    def test_plugin_json_has_semver(self):
        with open(REPO_ROOT / ".claude-plugin" / "plugin.json") as f:
            data = json.load(f)
        parts = data["version"].split(".")
        assert len(parts) == 3
        assert all(p.isdigit() for p in parts), f"Version parts must be numeric: {data['version']}"

    def test_claude_md_mentions_versioning(self):
        content = (REPO_ROOT / "CLAUDE.md").read_text()
        assert "semver" in content.lower() or "Versioning" in content


class TestProjectFiles:
    """Validate top-level project files."""

    def test_readme_exists(self):
        assert (REPO_ROOT / "README.md").exists()

    def test_readme_has_installation(self):
        content = (REPO_ROOT / "README.md").read_text()
        assert "claude plugin marketplace add" in content
        assert "claude plugin install transcribe@transcribe" in content

    def test_license_exists(self):
        assert (REPO_ROOT / "LICENSE").exists()

    def test_license_is_mit(self):
        content = (REPO_ROOT / "LICENSE").read_text()
        assert "MIT License" in content

    def test_claude_md_exists(self):
        assert (REPO_ROOT / "CLAUDE.md").exists()

    def test_claude_md_has_pre_pr_checklist(self):
        content = (REPO_ROOT / "CLAUDE.md").read_text()
        assert "Pre-PR Checklist" in content

    def test_ci_workflow_exists(self):
        assert (REPO_ROOT / ".github" / "workflows" / "ci.yml").exists()

    def test_gitignore_excludes_config(self):
        content = (REPO_ROOT / ".gitignore").read_text()
        assert ".transcribe-config.json" in content

    def test_no_config_json_committed(self):
        """Host-specific config must not be in the repo."""
        assert not (REPO_ROOT / "skills" / "transcribe" / "config.json").exists()
        assert not (REPO_ROOT / ".transcribe-config.json").exists()


class TestSkillWorkflow:
    """Validate key workflow steps are present in SKILL.md."""

    @pytest.fixture
    def skill_content(self):
        return (REPO_ROOT / "skills" / "transcribe" / "SKILL.md").read_text()

    def test_has_video_detection(self, skill_content):
        assert "Detect Video & Extract Audio" in skill_content

    def test_has_cost_estimation(self, skill_content):
        assert "Estimate Cost" in skill_content

    def test_has_transfer_step(self, skill_content):
        assert "Transfer Audio to Server" in skill_content

    def test_has_transcription_step(self, skill_content):
        assert "Run Transcription" in skill_content

    def test_has_mcp_fallback(self, skill_content):
        """Skill must support both MCP tool and direct Python invocation."""
        assert "Approach A" in skill_content
        assert "Approach B" in skill_content

    def test_has_cleanup_step(self, skill_content):
        assert "Clean Up" in skill_content

    def test_has_output_formats(self, skill_content):
        assert "Summary + Transcript" in skill_content
        assert "Summary only" in skill_content
        assert "Transcript only" in skill_content

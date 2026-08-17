from __future__ import annotations

import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INSTALLER = ROOT / "scripts" / "install.sh"
SKILLS = {
    "finance-top-journal-writing",
    "finance-asset-pricing-writing",
    "finance-causal-empirical-writing",
    "finance-intermediation-markets-writing",
    "finance-theory-structural-writing",
}


class InstallerTests(unittest.TestCase):
    def run_installer(
        self,
        *args: str,
        home: Path,
        codex_home: Path | None = None,
        installer: Path = INSTALLER,
        check: bool = True,
    ) -> subprocess.CompletedProcess[str]:
        env = os.environ.copy()
        env["HOME"] = str(home)
        if codex_home is None:
            env.pop("CODEX_HOME", None)
        else:
            env["CODEX_HOME"] = str(codex_home)
        return subprocess.run(
            [str(installer), *args],
            cwd=installer.parent.parent,
            env=env,
            text=True,
            capture_output=True,
            check=check,
        )

    def make_installer_fixture(self, root: Path) -> tuple[Path, Path, list[str]]:
        release = root / "release"
        installer = release / "scripts" / "install.sh"
        skill = release / "skills" / "finance-top-journal-writing"
        shutil.copytree(INSTALLER.parent, installer.parent)

        formal_files = {
            "SKILL.md": "---\nname: finance-top-journal-writing\ndescription: Test.\n---\n",
            "agents/openai.yaml": "interface:\n  display_name: Test\n",
            "references/guide.md": "# Guide\n",
            "assets/templates/example.bin": "asset\n",
            "scripts/tool.py": "print('ok')\n",
        }
        for relative, contents in formal_files.items():
            path = skill / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(contents, encoding="utf-8")

        return installer, skill, list(formal_files)

    def test_default_installs_all_to_current_user_location(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            home = Path(temp_dir)
            self.run_installer(home=home)
            target = home / ".agents" / "skills"
            self.assertEqual({path.name for path in target.iterdir()}, SKILLS)
            for skill in SKILLS:
                self.assertTrue((target / skill / "SKILL.md").is_file())

    def test_explicit_codex_home_is_honored(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            home = Path(temp_dir) / "home"
            codex_home = Path(temp_dir) / "custom-codex"
            home.mkdir()
            self.run_installer(
                "finance-top-journal-writing",
                home=home,
                codex_home=codex_home,
            )
            self.assertTrue(
                (codex_home / "skills" / "finance-top-journal-writing" / "SKILL.md").is_file()
            )
            self.assertFalse((home / ".agents" / "skills").exists())

    def test_existing_install_requires_replace(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            home = Path(temp_dir)
            self.run_installer("finance-top-journal-writing", home=home)
            result = self.run_installer(
                "finance-top-journal-writing", home=home, check=False
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("use --replace", result.stderr)

    def test_replace_backs_up_outside_discovery_root(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            home = Path(temp_dir)
            self.run_installer("finance-top-journal-writing", home=home)
            target = home / ".agents" / "skills"
            marker = target / "finance-top-journal-writing" / "user-marker.txt"
            marker.write_text("preserve me", encoding="utf-8")

            self.run_installer(
                "--replace", "finance-top-journal-writing", home=home
            )

            self.assertFalse(marker.exists())
            self.assertFalse(any("backup" in path.name for path in target.iterdir()))
            backups = list(
                (home / ".agents" / "skills.backups").glob(
                    "finance-top-journal-writing.*"
                )
            )
            self.assertEqual(len(backups), 1)
            self.assertEqual(
                (backups[0] / "user-marker.txt").read_text(encoding="utf-8"),
                "preserve me",
            )

    def test_git_checkout_copies_only_tracked_skill_files(self) -> None:
        if shutil.which("git") is None:
            self.skipTest("git is not available")

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            installer, source_skill, formal_files = self.make_installer_fixture(root)
            release = installer.parent.parent
            subprocess.run(["git", "init", "-q"], cwd=release, check=True)
            subprocess.run(["git", "add", "scripts", "skills"], cwd=release, check=True)

            junk_files = [
                source_skill / "__pycache__" / "cache.pyc",
                source_skill / ".DS_Store",
                source_skill / "scratch-not-for-release.txt",
                source_skill / "references" / "untracked-notes.md",
            ]
            for path in junk_files:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("junk", encoding="utf-8")

            home = root / "home"
            home.mkdir()
            target_root = root / "installed"
            self.run_installer(
                "--target",
                str(target_root),
                "finance-top-journal-writing",
                home=home,
                installer=installer,
            )

            installed = target_root / "finance-top-journal-writing"
            for relative in formal_files:
                self.assertTrue((installed / relative).is_file(), relative)
            for source_junk in junk_files:
                relative = source_junk.relative_to(source_skill)
                self.assertFalse((installed / relative).exists(), str(relative))

    def test_release_archive_uses_standard_structure_and_filters_junk(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            installer, source_skill, formal_files = self.make_installer_fixture(root)
            junk_files = [
                source_skill / "README.md",
                source_skill / ".DS_Store",
                source_skill / "scripts" / "__pycache__" / "tool.pyc",
                source_skill / "references" / "draft.tmp",
                source_skill / "references" / ".cache" / "hidden.md",
                source_skill / "references" / "rejected.orig",
                source_skill / "assets" / "editor-backup.md~",
            ]
            for path in junk_files:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("junk", encoding="utf-8")

            home = root / "home"
            home.mkdir()
            target_root = root / "installed"
            self.run_installer(
                "--target",
                str(target_root),
                "finance-top-journal-writing",
                home=home,
                installer=installer,
            )

            installed = target_root / "finance-top-journal-writing"
            for relative in formal_files:
                self.assertTrue((installed / relative).is_file(), relative)
            for source_junk in junk_files:
                relative = source_junk.relative_to(source_skill)
                self.assertFalse((installed / relative).exists(), str(relative))


if __name__ == "__main__":
    unittest.main()

from __future__ import annotations

import os
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
        check: bool = True,
    ) -> subprocess.CompletedProcess[str]:
        env = os.environ.copy()
        env["HOME"] = str(home)
        if codex_home is None:
            env.pop("CODEX_HOME", None)
        else:
            env["CODEX_HOME"] = str(codex_home)
        return subprocess.run(
            [str(INSTALLER), *args],
            cwd=ROOT,
            env=env,
            text=True,
            capture_output=True,
            check=check,
        )

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


if __name__ == "__main__":
    unittest.main()

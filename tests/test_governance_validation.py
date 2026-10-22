import io
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

from scripts.validate_governance import REQUIRED_RULES, main, validate_text


def valid_document() -> str:
    sections = "\n".join(f"## {number}. Section {number}" for number in range(1, 13))
    rules = "\n".join(REQUIRED_RULES.values())
    return f"# Governance\n{sections}\n{rules}\n"


class GovernanceValidatorTests(unittest.TestCase):
    def test_accepts_document_with_all_required_sections_and_rules(self):
        self.assertEqual(validate_text(valid_document()), [])

    def test_rejects_empty_document(self):
        self.assertIn("README.md is empty.", validate_text("  \n"))

    def test_rejects_each_missing_numbered_section(self):
        document = valid_document()
        for number in range(1, 13):
            with self.subTest(section=number):
                heading = f"## {number}. Section {number}\n"
                errors = validate_text(document.replace(heading, "", 1))
                self.assertTrue(
                    any(f"section: {number}" in error for error in errors),
                    msg=f"Validator did not report missing section {number}: {errors}",
                )

    def test_rejects_heading_number_only_inside_prose(self):
        content = valid_document().replace(
            "## 4. Section 4",
            "The text mentions ## 4. but is not a heading",
        )
        errors = validate_text(content)
        self.assertTrue(any("section: 4" in error for error in errors))

    def test_rejects_each_missing_mandatory_rule(self):
        document = valid_document()
        for name, phrase in REQUIRED_RULES.items():
            with self.subTest(rule=name):
                errors = validate_text(document.replace(phrase, "", 1))
                self.assertTrue(
                    any("mandatory governance rule" in error for error in errors),
                    msg=f"Validator did not report missing rule {name}: {errors}",
                )

    def test_cli_rejects_missing_argument(self):
        output = io.StringIO()
        with patch("sys.argv", ["scripts/validate_governance.py"]), redirect_stdout(output):
            result = main()
        self.assertEqual(result, 2)
        self.assertIn("Usage:", output.getvalue())

    def test_cli_rejects_missing_file(self):
        with tempfile.TemporaryDirectory() as directory:
            missing_path = Path(directory) / "missing.md"
            output = io.StringIO()
            with patch(
                "sys.argv", ["scripts/validate_governance.py", str(missing_path)]
            ), redirect_stdout(output):
                result = main()
        self.assertEqual(result, 1)
        self.assertIn("file not found", output.getvalue())

    def test_cli_rejects_invalid_utf8(self):
        with tempfile.TemporaryDirectory() as directory:
            invalid_path = Path(directory) / "invalid.md"
            invalid_path.write_bytes(b"\xff\xfe\xfa")
            output = io.StringIO()
            with patch(
                "sys.argv", ["scripts/validate_governance.py", str(invalid_path)]
            ), redirect_stdout(output):
                result = main()
        self.assertEqual(result, 1)
        self.assertIn("cannot read", output.getvalue())

    def test_cli_reports_the_actual_validated_path(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "governance-check.md"
            target.write_text(valid_document(), encoding="utf-8")
            output = io.StringIO()
            with patch(
                "sys.argv", ["scripts/validate_governance.py", str(target)]
            ), redirect_stdout(output):
                result = main()
        self.assertEqual(result, 0)
        self.assertIn(f"PASS: {target} exists and is non-empty.", output.getvalue())
        self.assertNotIn("PASS: README.md exists", output.getvalue())


    def test_end_to_end_cli_accepts_approved_repository_readme(self):
        repository_root = Path(__file__).resolve().parents[1]
        validator = repository_root / "scripts" / "validate_governance.py"
        readme = repository_root / "README.md"

        completed = subprocess.run(
            [sys.executable, str(validator), str(readme)],
            cwd=repository_root,
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(completed.returncode, 0, msg=completed.stdout + completed.stderr)
        self.assertIn(f"PASS: {readme} exists and is non-empty.", completed.stdout)
        self.assertIn("PASS: all 12 numbered governance sections are present.", completed.stdout)

    def test_end_to_end_cli_rejects_invalid_governance_document(self):
        repository_root = Path(__file__).resolve().parents[1]
        validator = repository_root / "scripts" / "validate_governance.py"
        invalid_document = valid_document().replace("## 4. Section 4\n", "", 1)
        invalid_document = invalid_document.replace(REQUIRED_RULES["final decision owner"], "", 1)

        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "invalid-governance.md"
            target.write_text(invalid_document, encoding="utf-8")
            completed = subprocess.run(
                [sys.executable, str(validator), str(target)],
                cwd=repository_root,
                capture_output=True,
                text=True,
                check=False,
            )

        self.assertEqual(completed.returncode, 1, msg=completed.stdout + completed.stderr)
        self.assertIn("Missing or invalid numbered governance section: 4", completed.stdout)
        self.assertIn("Missing mandatory governance rule: final decision owner", completed.stdout)


if __name__ == "__main__":
    unittest.main()

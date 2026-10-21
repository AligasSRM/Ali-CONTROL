import unittest

from scripts.validate_governance import REQUIRED_RULES, REQUIRED_HEADINGS, validate_text


def valid_document() -> str:
    sections = "\n".join(f"## {n}. Section {n}" for n in range(1, 8))
    rules = "\n".join(REQUIRED_RULES.values())
    headings = "\n".join(REQUIRED_HEADINGS)
    return f"# Governance\n{sections}\n{headings}\n{rules}\n"


class GovernanceValidatorTests(unittest.TestCase):
    def test_accepts_document_with_all_required_sections_and_rules(self):
        self.assertEqual(validate_text(valid_document()), [])

    def test_rejects_missing_numbered_section(self):
        content = valid_document().replace("## 4. Section 4\n", "")
        errors = validate_text(content)
        self.assertTrue(any("section: 4" in error for error in errors))

    def test_rejects_missing_mandatory_rule(self):
        phrase = next(iter(REQUIRED_RULES.values()))
        errors = validate_text(valid_document().replace(phrase, ""))
        self.assertTrue(any("mandatory rule" in error for error in errors))

    def test_rejects_missing_approval_record_heading(self):
        content = valid_document().replace("## سجل الاعتماد\n", "")
        errors = validate_text(content)
        self.assertTrue(any("سجل الاعتماد" in error for error in errors))

    def test_rejects_empty_document(self):
        self.assertIn("README is empty.", validate_text("  \n"))


if __name__ == "__main__":
    unittest.main()

import unittest

from scripts.validate_governance import REQUIRED_RULES, REQUIRED_HEADINGS, validate_text


def valid_document(use_approved_wording: bool = False) -> str:
    sections = "\n".join(f"## {n}. Section {n}" for n in range(1, 8))
    heading_index = 1 if use_approved_wording else 0
    headings = "\n".join(group[heading_index] for group in REQUIRED_HEADINGS)
    rules = "\n".join(
        alternatives[-1] if use_approved_wording and len(alternatives) > 1 else alternatives[0]
        for alternatives in REQUIRED_RULES.values()
    )
    return f"# Governance\n{sections}\n{headings}\n{rules}\n"


class GovernanceValidatorTests(unittest.TestCase):
    def test_accepts_document_with_all_required_sections_and_rules(self):
        self.assertEqual(validate_text(valid_document()), [])

    def test_accepts_equivalent_wording_from_approved_readme(self):
        self.assertEqual(validate_text(valid_document(use_approved_wording=True)), [])

    def test_rejects_missing_numbered_section(self):
        content = valid_document().replace("## 4. Section 4\n", "")
        errors = validate_text(content)
        self.assertTrue(any("section: 4" in error for error in errors))

    def test_rejects_missing_mandatory_rule(self):
        phrase = REQUIRED_RULES["explicit authorization"][0]
        errors = validate_text(valid_document().replace(phrase, ""))
        self.assertTrue(any("mandatory rule: explicit authorization" in error for error in errors))

    def test_rejects_missing_approval_record_heading(self):
        content = valid_document().replace(REQUIRED_HEADINGS[1][0] + "\n", "")
        errors = validate_text(content)
        self.assertTrue(any("سجل الاعتماد" in error for error in errors))

    def test_rejects_empty_document(self):
        self.assertIn("README is empty.", validate_text("  \n"))


if __name__ == "__main__":
    unittest.main()

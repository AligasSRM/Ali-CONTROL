import unittest

from scripts.validate_governance import REQUIRED_RULES, validate_text


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


if __name__ == "__main__":
    unittest.main()

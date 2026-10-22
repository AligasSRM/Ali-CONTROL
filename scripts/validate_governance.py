#!/usr/bin/env python3
"""Validate the approved Ali-Control README governance structure and rules."""

from pathlib import Path
import re
import sys

REQUIRED_RULES = {
    "final decision owner": "صاحب القرار النهائي",
    "repository entry authorization": "لا يجوز تجاوزها من دون توجيه صريح من علي",
    "no implicit permission for changes": "لا يُعدّ إذناً بالتعديل أو الحذف أو الدمج أو النشر أو تغيير إعدادات الحماية",
    "explicit approval for changes": "دون الموافقة الصريحة المطلوبة من علي",
    "no unapproved repository switching": "ولا ينتقل إلى مستودع آخر",
}


def validate_text(content: str) -> list[str]:
    """Return validation errors for a README's content."""
    errors: list[str] = []

    if not content.strip():
        return ["README.md is empty."]

    for number in range(1, 13):
        pattern = rf"^##\s+{number}\.\s+\S.*$"
        if not re.search(pattern, content, flags=re.MULTILINE):
            errors.append(f"Missing or invalid numbered governance section: {number}")

    for name, phrase in REQUIRED_RULES.items():
        if phrase not in content:
            errors.append(f"Missing mandatory governance rule: {name}")

    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python scripts/validate_governance.py <README path>")
        return 2

    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"FAIL: file not found: {path}")
        return 1

    try:
        content = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        print(f"FAIL: cannot read {path}: {error}")
        return 1

    errors = validate_text(content)
    if errors:
        print("FAIL: Ali-Control governance validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PASS: README.md exists and is non-empty.")
    print("PASS: all 12 numbered governance sections are present.")
    print("PASS: core ownership, authorization, and repository-entry safeguards are present.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

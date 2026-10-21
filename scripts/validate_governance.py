#!/usr/bin/env python3
"""Validate the required structure and governance clauses of a README."""

from pathlib import Path
import re
import sys

REQUIRED_RULES = {
    "final decision owner": "صاحب القرار النهائي",
    "explicit authorization": "لا ينفّذ أليكس أي تغيير غير مشمول بتفويض واضح",
    "repository separation": "لا ينتقل أليكس إلى مشروع آخر من تلقاء نفسه",
    "secret protection": "لا تُعرض كلمات المرور أو مفاتيح الوصول",
    "evidence-based completion": "عند نقص الأدلة، لا تُصنّف المهمة أخضر",
    "verified documentation": "لا يؤكد أليكس حفظ التوثيق أو نشره إلا بعد التحقق",
    "GitHub protection evidence": "لا تُعد القاعدة فعّالة تقنياً لمجرد كتابتها",
    "approval before policy changes": "موافقة صريحة من علي قبل تطبيقها",
}

REQUIRED_HEADINGS = (
    "## الملخص التنفيذي",
    "## سجل الاعتماد",
)


def validate_text(content: str) -> list[str]:
    errors: list[str] = []

    if not content.strip():
        return ["README is empty."]

    for number in range(1, 8):
        pattern = rf"^##\s+{number}\.\s+\S.*$"
        if not re.search(pattern, content, flags=re.MULTILINE):
            errors.append(f"Missing or invalid numbered section: {number}")

    for heading in REQUIRED_HEADINGS:
        if heading not in content:
            errors.append(f"Missing required heading: {heading}")

    for name, phrase in REQUIRED_RULES.items():
        if phrase not in content:
            errors.append(f"Missing mandatory rule: {name}")

    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python scripts/validate_governance.py <README path>")
        return 2

    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"FAIL: file not found: {path}")
        return 1

    errors = validate_text(path.read_text(encoding="utf-8"))
    if errors:
        print("FAIL: governance validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PASS: all required sections, headings, and governance rules are present.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

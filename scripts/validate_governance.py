#!/usr/bin/env python3
"""Validate required governance structure and equivalent approved clauses."""

from pathlib import Path
import re
import sys

# Each rule accepts the proposed canonical wording and known equivalent wording
# already used by the approved README on main. Keep alternatives meaning-specific.
REQUIRED_RULES = {
    "final decision owner": ("صاحب القرار النهائي",),
    "explicit authorization": (
        "لا ينفّذ أليكس أي تغيير غير مشمول بتفويض واضح",
        "لا يُنفّذ أي تعديل أو حذف أو دمج أو نشر أو تغيير حساس",
        "لا يُنفّذ أي تغيير خارج النطاق الموافق عليه",
    ),
    "repository separation": (
        "لا ينتقل أليكس إلى مشروع آخر من تلقاء نفسه",
        "لا ينتقل أليكس بين المشاريع من تلقاء نفسه",
    ),
    "secret protection": (
        "لا تُعرض كلمات المرور أو مفاتيح الوصول",
        "تُحمى كلمات المرور ومفاتيح الوصول",
        "لا تُعرض الأسرار في السجلات أو التقارير أو رسائل الأخطاء أو مخرجات الأوامر",
    ),
    "evidence-based completion": (
        "عند نقص الأدلة، لا تُصنّف المهمة أخضر",
        "لا يُعتمد اللون الأخضر لمجرد إنشاء ملف أو تشغيل أمر أو نجاح اختبار محدود",
        "ولا يُعلن الإغلاق الكامل قبل استيفاء معايير القبول",
    ),
    "verified documentation": (
        "لا يؤكد أليكس حفظ التوثيق أو نشره إلا بعد التحقق",
    ),
    "GitHub protection evidence": (
        "لا تُعد القاعدة فعّالة تقنياً لمجرد كتابتها",
        "لا يضمن وحده أن جميع الأدوات أو الوكلاء أو المحادثات سيقرؤونها تلقائياً",
        "وتُعد الحماية التقنية فعالة بالقدر الذي تثبته الإعدادات الفعلية والاختبارات والصلاحيات المطبقة",
    ),
    "approval before policy changes": (
        "موافقة صريحة من علي قبل تطبيقها",
        "أي تعديل لاحق على الوثيقة أو قواعدها يحتاج إلى عرض واضح للتغييرات المقترحة وموافقة صريحة من علي قبل تطبيقها",
    ),
}

# Heading alternatives support both the proposed labels and the headings in
# the currently approved README on main.
REQUIRED_HEADINGS = (
    ("## الملخص التنفيذي", "## 11. القاعدة التنفيذية المختصرة"),
    ("## سجل الاعتماد", "## 12. سجل اعتماد الوثيقة"),
)


def validate_text(content: str) -> list[str]:
    errors: list[str] = []

    if not content.strip():
        return ["README is empty."]

    for number in range(1, 8):
        pattern = rf"^##\s+{number}\.\s+\S.*$"
        if not re.search(pattern, content, flags=re.MULTILINE):
            errors.append(f"Missing or invalid numbered section: {number}")

    for alternatives in REQUIRED_HEADINGS:
        if not any(heading in content for heading in alternatives):
            errors.append(f"Missing required heading: {' OR '.join(alternatives)}")

    for name, alternatives in REQUIRED_RULES.items():
        if not any(phrase in content for phrase in alternatives):
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

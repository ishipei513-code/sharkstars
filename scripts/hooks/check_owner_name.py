#!/usr/bin/env python3
"""
PreToolUse hook: block edits that introduce a wrong owner/representative name
into SHARKSTARS files.

Canonical owner: 石橋昇平 (Ishibashi Shohei). This hook fires on Write/Edit
and refuses if a representative-name slot is being filled with anything else.

Stdin: Claude Code hook JSON envelope.
Exit:  0 = allow, 2 = block (stderr is shown to Claude).
"""
import json
import re
import sys

CANONICAL_FAMILY = "石橋"
CANONICAL_FULL_VARIANTS = ("石橋昇平", "石橋 昇平", "Ishibashi Shohei", "Ishibashi", "石橋")

# Historical mistakes — always block on sight, anywhere in owner context.
KNOWN_BAD_NAMES = ("石井",)

# Patterns that mark a "this is the representative's name" slot.
# Each pattern's group(1) is the name we need to validate.
OWNER_SLOT_PATTERNS = [
    re.compile(r'代表者?[\s　]*[:：][\s　]*([^\n<,，、|｜]{1,40})'),
    re.compile(r'代表[\s　]*[:：][\s　]*([^\n<,，、|｜]{1,40})'),
    re.compile(r'"familyName"\s*:\s*"([^"]{1,40})"'),
    re.compile(r'"givenName"\s*:\s*"([^"]{1,40})"'),
    re.compile(r'"name"\s*:\s*"([^"]{1,40})"\s*,\s*"jobTitle"\s*:\s*"代表'),
    re.compile(r'<div class="party-name">([^<]{1,40})</div>'),
    re.compile(r'<div class="sig-name">([^<]{1,40})</div>'),
    re.compile(r'class="hanko"[^>]*>([^<]{1,10})</div>'),
    re.compile(r'(?i)Founder[\s:：]+([^\n<,]{1,40})'),
    re.compile(r'運営責任者[\s　]*[:：]?[\s　]*\n?\s*<td>([^<]{1,40})</td>'),
]


def extract_new_content(payload: dict) -> str:
    """Pull the text being written/edited out of the hook JSON envelope."""
    tool_input = payload.get("tool_input") or {}
    pieces = []
    # Write tool
    if "content" in tool_input:
        pieces.append(str(tool_input["content"]))
    # Edit tool
    if "new_string" in tool_input:
        pieces.append(str(tool_input["new_string"]))
    # MultiEdit-style edits array
    edits = tool_input.get("edits")
    if isinstance(edits, list):
        for e in edits:
            if isinstance(e, dict) and "new_string" in e:
                pieces.append(str(e["new_string"]))
    return "\n".join(pieces)


def normalize(name: str) -> str:
    return re.sub(r"[\s　]+", "", name).strip()


def is_canonical(name: str) -> bool:
    n = normalize(name)
    if not n:
        return True  # empty match is not an assertion of a wrong name
    return n in {normalize(v) for v in CANONICAL_FULL_VARIANTS}


def find_violations(content: str) -> list[str]:
    violations = []

    # Hard denylist — if any known-bad name appears in owner context, fail.
    for bad in KNOWN_BAD_NAMES:
        # Look for the bad name within ~30 chars of an owner keyword.
        pattern = re.compile(
            r"(代表|代表者|Founder|familyName|party-name|sig-name|hanko|運営責任者)"
            r"[\s\S]{0,40}?" + re.escape(bad)
        )
        if pattern.search(content):
            violations.append(
                f"Owner-context contains forbidden name '{bad}'. "
                f"Canonical owner is 石橋昇平."
            )

    # Slot patterns — value in the slot must be a canonical variant.
    for pat in OWNER_SLOT_PATTERNS:
        for m in pat.finditer(content):
            value = m.group(1)
            if not is_canonical(value):
                # Allow givenName=昇平 alone (canonical given name) — handle here
                if normalize(value) in {"昇平", "Shohei"}:
                    continue
                violations.append(
                    f"Owner slot matched by /{pat.pattern[:60]}.../ has "
                    f"non-canonical value: {value!r}. Expected 石橋昇平."
                )

    return violations


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception as e:
        # If we can't parse, do not block — let Claude proceed.
        print(f"check_owner_name: hook payload parse error: {e}", file=sys.stderr)
        return 0

    content = extract_new_content(payload)
    if not content:
        return 0

    violations = find_violations(content)
    if not violations:
        return 0

    print("BLOCKED by check_owner_name.py — owner/representative name guard:", file=sys.stderr)
    for v in violations:
        print(f"  - {v}", file=sys.stderr)
    print(
        "\nIf this is a legitimate edit (e.g., listing a third-party name in "
        "regular content), tell the user before retrying. Do NOT auto-bypass.",
        file=sys.stderr,
    )
    return 2


if __name__ == "__main__":
    sys.exit(main())

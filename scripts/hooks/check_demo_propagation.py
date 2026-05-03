#!/usr/bin/env python3
"""
PostToolUse hook: when a demo's index.html is edited, surface a reminder
that the same change might need to propagate to the other 55 demo sites.

Strategy: keep it advisory, not blocking. The hook only emits a notice when
the edited path matches demos/<slug>/index.html and the change touched a
selector / class / meta-tag pattern that the other demos likely share.

Stdin: Claude Code hook JSON envelope.
Exit:  0 always (advisory). Output goes to stderr so Claude sees it.
"""
import json
import os
import re
import sys
from pathlib import Path

DEMO_PATH_RE = re.compile(r"demos[\\/]([a-z0-9-]+)[\\/]index\.html$", re.IGNORECASE)

# If the diff touches any of these, it's a horizontally-significant change.
HORIZONTAL_SIGNALS = [
    re.compile(r'<meta\s+(?:name|property)="(?:og:|twitter:|description|keywords)'),
    re.compile(r'<link\s+rel="canonical"'),
    re.compile(r'application/ld\+json'),
    re.compile(r'class="hdr"'),
    re.compile(r'class="menu-toggle"'),
    re.compile(r'class="sect"'),
    re.compile(r'data-lucide='),
    re.compile(r'lang="ja"'),
]


def extract_changed_text(payload: dict) -> tuple[str, str]:
    """Return (file_path, changed_text) from the hook envelope."""
    tool_input = payload.get("tool_input") or {}
    file_path = tool_input.get("file_path", "")
    pieces = []
    if "content" in tool_input:
        pieces.append(str(tool_input["content"]))
    if "new_string" in tool_input:
        pieces.append(str(tool_input["new_string"]))
    edits = tool_input.get("edits")
    if isinstance(edits, list):
        for e in edits:
            if isinstance(e, dict) and "new_string" in e:
                pieces.append(str(e["new_string"]))
    return file_path, "\n".join(pieces)


def matched_signals(text: str) -> list[str]:
    hits = []
    for pat in HORIZONTAL_SIGNALS:
        if pat.search(text):
            hits.append(pat.pattern)
    return hits


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0

    file_path, text = extract_changed_text(payload)
    if not file_path or not text:
        return 0

    m = DEMO_PATH_RE.search(file_path.replace("\\", "/"))
    if not m:
        return 0
    edited_slug = m.group(1)

    signals = matched_signals(text)
    if not signals:
        return 0

    # Count peer demos.
    repo_root = Path(__file__).resolve().parents[2]
    demos_dir = repo_root / "demos"
    peers = []
    if demos_dir.is_dir():
        for entry in sorted(os.listdir(demos_dir)):
            if entry == edited_slug:
                continue
            if (demos_dir / entry / "index.html").is_file():
                peers.append(entry)

    if not peers:
        return 0

    print(
        f"\n[demo-propagation reminder] You edited demos/{edited_slug}/index.html "
        f"and the change touched {len(signals)} horizontally-significant pattern(s):",
        file=sys.stderr,
    )
    for s in signals:
        print(f"  - /{s}/", file=sys.stderr)
    print(
        f"\n  {len(peers)} peer demo(s) likely share this pattern. "
        f"Decide whether the same change should propagate. "
        f"Use the demo-site-reviewer subagent in parallel to spot-check.",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

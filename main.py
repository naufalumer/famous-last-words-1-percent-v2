"""Famous Last Words at 1 Percent - v2.

Writes the user's own last-words line (a single line, 156 chars) to
$MAKEFUN_OUTPUT_DIR/entry.txt. Standard library only.
"""

import os

ENTRY = "Bro I come home to absolutely nothing I'm just a lonely guy loaded with money Nobody told me my days won't be sunny I'm bleeding on people who didn't cut me"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY
    assert 1 <= len(text) <= 199, f"entry must be 1-199 chars, got {len(text)}"
    assert text.strip(), "entry must not be only whitespace"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8") as f:
        assert f.read() == text, "read-back mismatch"


if __name__ == "__main__":
    main()

"""Entry for make.fun: The Most Boring Object, Reviewed in One Line.

Writes one review (max 200 chars, one line) to entry.txt in
MAKEFUN_OUTPUT_DIR (default /output). The review is a rubber band:
six years of loyal service, then it snaps the one morning it is
actually needed — the object's own dullness is the joke.
"""

import os
import stat

ENTRY = "This rubber band held 47 letters together for six years, then snapped the morning I finally needed one."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY
    assert 1 <= len(text) <= 200, "entry must be 1-200 chars"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)

if __name__ == "__main__":
    main()

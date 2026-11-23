"""Dad Joke Showdown entry (KA, food/kitchen angle).

One dad joke about the fridge and its leftovers, told the way a father
would say it across the dinner table: a straight-faced setup, then the
leftovers themselves ask the question, so the pun comes from their own
mouth in one clean beat — no reply, no dialogue tag, just the leftovers
wondering out loud. The turn is "still cool": the leftovers are
literally cold, and they ask about the relationship as if the fridge were
a friendship to check on — one question, two meanings, zero fat.
Every word earns its place; the punchline arrives at the very end,
exactly where a dad joke's should.
"""

import os
import sys

TEXT = "I opened the fridge and the leftovers asked, 'Are we still cool?'"


def main() -> int:
    """Write the joke to entry.txt, gated to 1-200 characters."""
    if not TEXT or not TEXT.strip():
        print("error: entry is empty or whitespace-only", file=sys.stderr)
        return 1
    if len(TEXT) > 200:
        print(f"error: entry is {len(TEXT)} characters, over the 200 limit", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != TEXT:
        print("error: read-back does not match TEXT byte-for-byte", file=sys.stderr)
        return 1
    print(f"wrote {path} ({len(TEXT)} characters)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

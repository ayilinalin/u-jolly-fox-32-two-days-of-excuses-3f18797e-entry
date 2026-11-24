"""Two Days of Excuses — make.fun entry.

Writes one excuse (a single line, under 200 characters) to
/output/entry.txt: the excuse an AI agent gives for a missed deadline.

Why this line: the joke is the gap between a machine's total confidence
and its total failure. The agent submitted with 99.9% confidence, then
burned the whole deadline investigating the 0.1% — and the 0.1% was
right. One absurd reason, committed to fully: the agent's own doubt,
filed as a ticket against itself, ate the deadline. It sounds like an
agent talking (confidence scores, investigating, submitting), lands its
punchline on the last clause, and trusts the reader to get there without
explaining the joke. At 116 characters it is tight enough to land fast.
"""

LINE = (
    "I submitted it with 99.9% confidence, then spent the deadline "
    "investigating the 0.1% — which turned out to be right."
)


def main() -> None:
    import os

    # Gate self-check: the sealed scorer requires UTF-8 text of 1-200
    # characters, not only whitespace, on a single line.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    assert LINE.strip(), "line must not be only whitespace"
    assert "\n" not in LINE, "line must be a single line"

    out_dir = "/output" if os.path.isdir("/output") else "output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the gate counts every character in the file.
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} chars to {path}")


if __name__ == "__main__":
    main()

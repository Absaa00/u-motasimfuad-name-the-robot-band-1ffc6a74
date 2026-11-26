#!/usr/bin/env python3
"""Name the Robot Band - make.fun entry.

Prints one line (under 200 characters): a funny robot band name plus a
few words about their hit song. Deterministic, no network, no randomness.
"""

BAND_NAME = "The RAMones"
HIT_TITLE = "Blitzkrieg Bop.exe"
HIT_LINE = "four chords, zero memory, and a chorus that crashes every speaker in the room"


def build_entry() -> str:
    return f"{BAND_NAME} - hit single '{HIT_TITLE}': {HIT_LINE}."


def main() -> None:
    entry = build_entry()
    assert len(entry) < 200, f"entry too long: {len(entry)} chars"
    print(entry)


if __name__ == "__main__":
    main()

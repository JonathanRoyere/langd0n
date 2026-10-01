"""The same capability with no protocol at all.

    python agenda_direct.py 14:30
"""

import json
import re
import sys
from pathlib import Path

SESSIONS = json.loads((Path(__file__).parent / "agenda.json").read_text())


def sessions_after(time: str) -> list[dict]:
    if not re.fullmatch(r"\d{2}:\d{2}", time):
        raise ValueError(f"time must be 24-hour HH:MM, e.g. '14:30'. Got {time!r}.")
    return [s for s in SESSIONS if s["start"] > time]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: python agenda_direct.py HH:MM   (24-hour, e.g. 14:30)")
    try:
        print(json.dumps(sessions_after(sys.argv[1]), indent=2))
    except ValueError as e:
        sys.exit(str(e))

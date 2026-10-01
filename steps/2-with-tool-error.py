"""An MCP server over today's conference agenda.

Run by the MCP client, not by you. See .vscode/mcp.json.
"""

import json
import re
from pathlib import Path

from mcp.server.mcpserver import MCPServer
from mcp.server.mcpserver.exceptions import ToolError

AGENDA = Path(__file__).parent / "agenda.json"

mcp = MCPServer(name="agenda")


@mcp.tool()
def list_sessions() -> list[dict]:
    """Return every session at today's conference, with start time, speaker,
    and title."""
    return json.loads(AGENDA.read_text())


@mcp.tool()
def sessions_after(time: str) -> list[dict]:
    """Returns sessions after the given time."""
    if not re.fullmatch(r"\d{2}:\d{2}", time):
        raise ToolError(f"time must be 24-hour HH:MM, e.g. '14:30'. Got {time!r}.")
    sessions = json.loads(AGENDA.read_text())
    return [s for s in sessions if s["start"] > time]


if __name__ == "__main__":
    mcp.run()

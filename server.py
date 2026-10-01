"""An MCP server over today's conference agenda.

Run by the MCP client, not by you. See .vscode/mcp.json.
"""

import json
from pathlib import Path

from mcp.server.mcpserver import MCPServer

AGENDA = Path(__file__).parent / "agenda.json"

mcp = MCPServer(name="agenda")


@mcp.tool()
def list_sessions() -> list[dict]:
    """Return every session at today's conference, with start time, speaker,
    and title."""
    return json.loads(AGENDA.read_text())


if __name__ == "__main__":
    mcp.run()

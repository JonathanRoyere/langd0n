# MCP Servers: The Agentic API Layer

Workshop template for Agentic 101 deliveries.

We build an MCP server over the conference's own agenda, then use it from
Copilot in agent mode, then work out when you should not have bothered.

## Start here

Open this repo in a GitHub Codespace. Dependencies install themselves. Then:

1. Open the Copilot Chat panel and put it in **Agent** mode.
2. VS Code asks you to trust the MCP server this workspace defines. Say yes.
   The server does not start until you do.
3. Ask: *what time is the MCP talk?*

If nothing happens, run **MCP: List Servers** from the command palette and
check the server's output log.

Copilot calls `list_sessions` on the server in `server.py`, which is already
wired up in `.vscode/mcp.json`. That is an MCP server. There isn't more to it.

## What's here

| File | What it is |
|---|---|
| `server.py` | the MCP server, ~15 lines of it |
| `agenda.json` | today's schedule |
| `agenda_direct.py` | the same lookup with no protocol, for comparison |
| `.vscode/mcp.json` | how the editor finds the server |
| `steps/` | finished states, if you fall behind |

## Checkpoints

If your copy stops working, or you want to skip ahead, copy a finished state
over `server.py` and reload the server:

```
cp steps/1-sessions_after.py    server.py
cp steps/2-with-tool-error.py   server.py
cp steps/3-with-description.py  server.py
```

See `steps/README.md` for what each one is.

## Note on the SDK

This uses `mcp` 2.x, where the server class is `MCPServer`:

```python
from mcp.server.mcpserver import MCPServer
```

Most examples you will find online are 1.x and use `FastMCP`. They will not
run against this. The rename is recent :)

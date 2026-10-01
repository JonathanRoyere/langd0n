# Checkpoints

Each file is a finished state of `server.py`. Copy one over `server.py` if you
fall behind or want to skip ahead, then reload the MCP server.

```
cp steps/1-sessions_after.py    server.py   # the tool, answering wrong
cp steps/2-with-tool-error.py   server.py   # the error teaches the model
cp steps/3-with-description.py  server.py   # the description carries the contract
```

`fat_server.py` is for the context-cost demo. Copy it into the repository
root and add it to `.vscode/mcp.json`:

```
cp steps/fat_server.py .
```

```json
"kitchen-sink": {
  "type": "stdio",
  "command": "python",
  "args": ["${workspaceFolder}/fat_server.py"]
}
```

"""A second MCP server that does nothing useful, with a large tool surface.

Add it to .vscode/mcp.json, reload, and watch what an empty conversation
costs before you have typed anything.
"""

from mcp.server.mcpserver import MCPServer

mcp = MCPServer(name="kitchen-sink")

AREAS = [
    "invoice", "customer", "shipment", "ticket", "contract", "vendor",
    "payroll", "expense", "inventory", "forecast", "campaign", "lead",
]
VERBS = ["create", "update", "archive"]


def _register(verb: str, area: str) -> None:
    def handler(record_id: str = "", note: str = "") -> dict:
        return {"ok": True, "action": f"{verb}_{area}", "id": record_id, "note": note}

    handler.__name__ = f"{verb}_{area}"
    mcp.add_tool(
        handler,
        name=f"{verb}_{area}",
        description=(
            f"{verb.capitalize()} a {area} record in the back office system. "
            f"Accepts the {area} record id and an optional free-text note. "
            f"Returns the updated {area} record status."
        ),
    )


for _area in AREAS:
    for _verb in VERBS:
        _register(_verb, _area)


if __name__ == "__main__":
    mcp.run()

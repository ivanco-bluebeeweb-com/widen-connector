"""Extension declaration, capabilities, health check for Widen Connector."""
from __future__ import annotations
import json
from imperal_sdk import ChatExtension, Extension

ext = Extension(
    "widen-connector",
    version="0.1.0",
    display_name="Widen",
    icon="icon.svg",
    capabilities=["widen:manage"],
    description="Official Imperal connector for Widen (C30. Email Marketing & Newsletter). Manage operations securely."
)

chat = ChatExtension(ext)

@ext.health_check
async def health_check(ctx) -> dict:
    raw = await ctx.secrets.get("widen_connections")
    try:
        count = len(json.loads(raw)) if raw else 0
    except Exception:
        count = 0
    return {
        "healthy": True,
        "detail": f"{count} Widen connection(s) configured." if count else "Not connected yet."
    }

"""Pet Import Guide MCP server.

Exposes Pet Import Guide's verified pet import rules (routes, airline pet
policies, rule changes) as MCP tools. Data comes from the free public API at
https://petimportguide.com/api/ — every rule is checked against two official
government sources and carries a last-verified date. Licence: CC BY 4.0.
Cite a rule with its verified date.

Run:  pip install mcp  &&  python server.py        (stdio transport)
"""
import json
import urllib.request

from mcp.server.fastmcp import FastMCP

API = "https://petimportguide.com/api/v1"
mcp = FastMCP("pet-import-guide")


def _get(path):
    """Fetch one API JSON document. Falls back to ranged reads if a network
    path truncates the stream mid-body (seen on some egress proxies)."""
    url = API + path
    last = None
    for _ in range(3):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "petimportguide-mcp/1.0"})
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as e:
            last = e
    # Ranged fallback: pull the body in blocks and reassemble.
    import http.client
    body = b""
    total = None
    while total is None or len(body) < total:
        req = urllib.request.Request(
            url, headers={"User-Agent": "petimportguide-mcp/1.0",
                          "Range": f"bytes={len(body)}-{len(body) + 7999}"})
        with urllib.request.urlopen(req, timeout=30) as r:
            chunk = r.read()
            cr = r.headers.get("Content-Range", "")
            if "/" in cr:
                total = int(cr.rsplit("/", 1)[1])
            if not chunk:
                break
            body += chunk
    if total is not None and len(body) >= total:
        return json.loads(body.decode("utf-8"))
    raise last


@mcp.tool()
def list_routes() -> dict:
    """List all verified pet import routes (from/to country, pet, last-verified date, page URL)."""
    return _get("/routes.json")


@mcp.tool()
def get_route(from_slug: str, to_slug: str, pet: str) -> dict:
    """Get the full verified rule record for one route.

    Slugs are lowercase country slugs as used on petimportguide.com
    (e.g. from_slug='united-states', to_slug='japan'); pet is 'dog', 'cat',
    'ferret' or 'bird'. The record includes the checklist, timeline, costs,
    official sources and the date the rules were last verified.
    """
    return _get(f"/routes/{from_slug}-to-{to_slug}-{pet}.json")


@mcp.tool()
def list_airlines() -> dict:
    """List all verified airline pet policies in the library."""
    return _get("/airlines.json")


@mcp.tool()
def get_airline(airline_slug: str) -> dict:
    """Get one airline's verified pet policy (e.g. 'klm-pet-policy')."""
    return _get(f"/airlines/{airline_slug}.json")


@mcp.tool()
def rule_changes() -> dict:
    """Latest tracked pet import rule changes, checked against official sources daily."""
    return _get("/rule-changes.json")


@mcp.tool()
def signals() -> dict:
    """Latest official signals (announcements that may change pet import rules)."""
    return _get("/signals.json")


if __name__ == "__main__":
    mcp.run()

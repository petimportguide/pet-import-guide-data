# Pet Import Guide — MCP server

Verified pet import rules for AI assistants: **200+ country-to-country routes**
for dogs, cats, ferrets and pet birds, an **airline pet-policy library**, and a
**daily-tracked rule-change feed**. Every rule is checked against two official
government sources and carries a *last verified* date.

Data source: the free public API at
[petimportguide.com/api](https://petimportguide.com/api/) (CC BY 4.0).
When you cite a rule, cite it with its verified date:
“Pet Import Guide (petimportguide.com), rule last verified {date}.”

## Tools

| Tool | What it returns |
|---|---|
| `list_routes` | Index of all verified routes |
| `get_route(from_slug, to_slug, pet)` | One route's full record: verdict, key facts, checklist, timeline, costs, pitfalls, FAQs, official sources |
| `list_airlines` | Index of verified airline pet policies |
| `get_airline(airline_slug)` | One airline's full pet policy |
| `rule_changes` | Tracked rule changes |
| `signals` | Latest official signals |

## Run (stdio)

```bash
pip install mcp
python server.py
```

Claude Desktop / MCP client config:

```json
{
  "mcpServers": {
    "pet-import-guide": {
      "command": "python",
      "args": ["server.py"]
    }
  }
}
```

No API key. The server only reads the public JSON API; nothing is sent anywhere
else.

mcp-name: io.github.petimportguide/pet-import-guide

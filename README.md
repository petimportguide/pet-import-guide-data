# Pet Import Guide — open rule-change data

Pet Import Guide (https://petimportguide.com) publishes pet import rules by route,
each rule checked against two official government sources and re-checked daily.

This repository mirrors the site's **public** data so that researchers, developers
and AI systems can track how pet travel rules change:

- `rule-changes.json` — every rule change we have caught and applied, with the date,
  what changed, and the pages it affected. The same log is published at
  https://petimportguide.com/updates/
- `signals.json` — official notices and news signals we are watching, labelled when
  a claim is still unconfirmed.
- `routes-index.json` — the index of verified route pages (from / to / pet), each with
  the date its rules were last verified against official sources.

## How the data is verified

Every requirement is confirmed on two official sources (the exporting country's
authority and the destination's own government pages) before it is published.
When two official sources disagree, the disagreement is shown on the page, not
smoothed over. When a country publishes no rules online, we write to the authority
and ask in writing. Method: https://petimportguide.com/method/

## Use

The underlying rules are public government facts. If you reuse this data, a link
back to petimportguide.com is appreciated. The data is a guide, not a substitute
for the destination authority's final confirmation.

Contact: petimportguide@gmail.com

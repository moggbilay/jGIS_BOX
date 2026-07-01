# jGIS BOX

**Version 1.0 — free distribution**

jGIS BOX is an ArcGIS Pro toolbox that links your own **Claude (Anthropic)** or
**OpenAI** account to your live map. It has **no AI of its own** — it sends your
plain‑language request plus the map's context to the AI, then runs the returned
`arcpy` code on your **active map** and shows the results, analysis, and new
layers.

**Drive ArcGIS Pro by typing, not coding.** Simple toolbox, no servers, no
dependencies, bring‑your‑own‑API‑key.

---

## Requirements
- ArcGIS Pro **3.2 or newer** (Python 3.11 / arcgispro-py3)
- Windows 64‑bit
- A Claude (Anthropic) or OpenAI **API key**

## Download & install
1. Download the files in **[`appdist/`](appdist)**:
   - `jGISBox.pyt` (the toolbox)
   - `jgisbox_core.cp311-win_amd64.pyd` (compiled code — keep it next to the `.pyt`)
   - `README.txt`
2. **Unblock** them (Windows blocks downloaded files): right‑click the ZIP →
   **Properties → Unblock** before extracting (or unblock each file after).
3. In ArcGIS Pro: **Catalog Pane → Toolboxes → Add Toolbox →** select `jGISBox.pyt`.

## Configure (once)
Run **jGIS BOX: Configure Claude**, paste your API key, pick a model
(default `claude-haiku-4-5`; use `claude-sonnet-4-6` or an Opus model for harder
analysis). Your key is stored **encrypted** for your Windows user in
`%USERPROFILE%\.arcgis_ai_agent\config.json`.

## Use
Open a map, run **jGIS BOX: Chat**, and type what you want, e.g.
> "How many parcels are owned by RCU?"
> "Select private commercial plots and add them to the map."

Full instructions are in [`appdist/README.txt`](appdist/README.txt).

---

## Data & privacy
Requests go over HTTPS to the AI provider you configured. It does **not** upload
your datasets wholesale — but whatever the agent **prints** during analysis
(attribute values, counts, sample rows) **is** sent to the provider. Don't use it
on data that must not leave your environment, and follow your organization's data
policy and the provider's usage policies.

## License (free distribution)
jGIS BOX is provided **free of charge**, **"as is", without warranty of any
kind**. The author is not liable for any data loss or damage — use at your own
risk and keep backups. You are responsible for your own API key, usage costs, and
compliance with the AI provider's and your organization's policies.

*Trademarks belong to their owners. "ArcGIS" is a trademark of Esri; this project
is not affiliated with or endorsed by Esri.*

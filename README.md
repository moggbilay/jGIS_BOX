# jGIS BOX

**Free distribution — ArcGIS Pro v1.2 · QGIS v1.0**

jGIS BOX is an ArcGIS Pro toolbox (and now a **QGIS plugin**) that links your own **Claude (Anthropic)** or
**OpenAI** account to your live map. It has **no AI of its own** — it sends your
plain‑language request plus the map's context to the AI, then runs the returned
`arcpy` code on your **active map** and shows the results, analysis, and new
layers.

**Drive ArcGIS Pro by typing, not coding.** Simple toolbox, no servers, no
dependencies, bring‑your‑own‑API‑key.

---

## Requirements
- ArcGIS Pro **3.0 or newer** (Python 3.9–3.13 / arcgispro-py3)
- Windows 64‑bit
- A Claude (Anthropic) or OpenAI **API key**

## Download & install
1. Download **all** files in **[`jGIS_BOX_ArcGIS_dist/`](jGIS_BOX_ArcGIS_dist)** into one folder:
   - `jGISBox.pyt` (the toolbox)
   - `jgisbox_core.pyd` (compiled code for ArcGIS Pro 3.3+)
   - `jgisbox_core.cp39-win_amd64.pyd` (compiled code for ArcGIS Pro 3.0–3.2)
   - `README.txt`

   Keep them together — Python automatically loads the right binary for your
   ArcGIS Pro version.
2. **Unblock** them (Windows blocks downloaded files): if you downloaded a ZIP,
   right‑click it → **Properties → Unblock** before extracting; otherwise unblock
   each file after downloading.
3. In ArcGIS Pro: **Catalog Pane → Toolboxes → Add Toolbox →** select `jGISBox.pyt`.

## Configure (once)
Run **jGIS BOX: Configure Claude**, paste your API key, pick a model
(default `claude-haiku-4-5`; use `claude-sonnet-4-6` or an Opus model for harder
analysis). Your key is stored **encrypted** for your Windows user in
`%USERPROFILE%\.arcgis_ai_agent\config.json`.

## Use
Open a map, run **jGIS BOX: Chat**, and type what you want, e.g.
> "How many features are in the active layer?"
> "Select features that meet a condition and add them to the map as a new layer."

**Session rules (optional):** in Configure you can set standing instructions that
load into **every** Chat automatically — e.g. "prefix all AI‑created outputs with
`AI_`" or "require an explicit workspace path before creating data" — so you don't
have to repeat them each session.

Full instructions are in [`jGIS_BOX_ArcGIS_dist/README.txt`](jGIS_BOX_ArcGIS_dist/README.txt).

---

## QGIS plugin (v1.0)
Same natural‑language control for your live **QGIS** project — bring‑your‑own‑key,
no servers. Works on **QGIS 3.x (Qt5) and 4.x (Qt6)**.

**Install** — from **[`jGIS_BOX_QGIS_dist/`](jGIS_BOX_QGIS_dist)** pick the zip for your QGIS:
- QGIS **3.x** → `jGIS_BOX_QGIS_3x.zip`
- QGIS **4.x** → `jGIS_BOX_QGIS_4x.zip`

Then in QGIS: **Plugins → Manage and Install Plugins → Install from ZIP →** select
that zip → Install, and tick **jGIS BOX** under *Installed*.

> Updating the plugin? **Close QGIS first**, then install the new zip — a compiled
> plugin can't be replaced while QGIS has it loaded.

Configure and use it exactly like the ArcGIS version: run **jGIS BOX: Configure**,
paste your key, pick a model, then open the **jGIS BOX** chat dock and type what you want.

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

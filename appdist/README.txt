============================================================
 jGIS BOX  -  AI assistant for ArcGIS Pro
 Version 1.0  (free distribution)
============================================================

Control the ACTIVE MAP in ArcGIS Pro with natural language.
The agent writes and runs arcpy code in your live session
(query, select, filter, analyze, geoprocess, symbolize, export).

(jGIS BOX is an independent tool. "ArcGIS" is a trademark of
 Esri; this product is not affiliated with or endorsed by Esri.)


REQUIREMENTS
------------
- ArcGIS Pro 3.2 or newer (Python 3.11 / arcgispro-py3).
- A Claude (Anthropic) or OpenAI API key.
- Windows 64-bit.


FILES (keep these two together in the same folder)
--------------------------------------------------
- jGISBox.pyt                       (the toolbox)
- jgisbox_core.cp311-win_amd64.pyd  (the compiled code)


STEP 1 - UNBLOCK THE FILES (important)
--------------------------------------
Windows blocks files that come from a zip/email/download, and
ArcGIS will then fail to load the tool. Fix it once:

  - Right-click the ZIP file -> Properties -> tick "Unblock" -> OK
  - THEN extract it.

(If you already extracted: right-click jgisbox_core.*.pyd ->
 Properties -> Unblock, and do the same for jGISBox.pyt.)

Extract to a normal local folder, e.g.  C:\Tools\jGISBox
(avoid OneDrive-synced folders).


STEP 2 - ADD THE TOOLBOX
------------------------
1. Open ArcGIS Pro and open your project (with a map + layers).
2. View -> Catalog Pane.
3. In the Catalog pane: right-click "Toolboxes" -> "Add Toolbox".
4. Browse to the folder and select jGISBox.pyt -> OK.
5. Expand the toolbox. You will see:
     - jGIS BOX: Configure Claude
     - jGIS BOX: Configure Codex
     - jGIS BOX: Chat


STEP 3 - CONFIGURE (one time)
-----------------------------
1. Double-click "jGIS BOX: Configure Claude".
2. Paste your API key.
3. Pick a model (default: claude-haiku-4-5 - cheapest; choose
   claude-sonnet-4-6 or an Opus model for harder analysis).
4. Run. It tests the key and confirms it works.

Your key is stored encrypted for your Windows user in:
   %USERPROFILE%\.arcgis_ai_agent\config.json


STEP 4 - USE IT
---------------
1. Make sure a map is OPEN and ACTIVE (click the map view).
2. Double-click "jGIS BOX: Chat" -> Run.
3. The chat window opens. Type what you want, e.g.:
     "How many parcels are owned by RCU?"
     "Select private commercial plots and add them to the map."

Notes:
- The Chat tool shows "Running..." the whole time the chat
  window is open. That is normal - CLOSE the chat window to
  finish the tool.
- Click "Log" in the chat window to watch live activity.
- "Auto-run steps" (below the message box): leave it on to let
  the agent work; turn it off to approve each step.


DATA & PRIVACY (what is sent to the AI)
---------------------------------------
This tool sends requests over HTTPS to the AI provider you
configured (Anthropic Claude or OpenAI). Nothing else leaves
your machine; your API key is stored locally (encrypted).

It does NOT upload your datasets, feature classes, geometry,
or files wholesale. On each turn it sends:
  - your typed messages;
  - a snapshot of the map: project/geodatabase paths, layer
    names, field names + aliases, data source paths, definition
    queries, and the spatial reference;
  - the code the agent writes; and
  - the PRINTED OUTPUT of running that code.

That last point matters: whatever the agent prints (attribute
values, counts, sample rows) IS sent to the provider. So real
data content can leave your machine during analysis - only the
parts that get printed, not the whole dataset.

Provider handling: Anthropic and OpenAI state that API data is
not used to train their models by default, with limited
retention for abuse monitoring. Confirm this against your
organization's data policy before using sensitive or restricted
data. If data must not leave your environment, do not use this
tool on that data.


TROUBLESHOOTING
---------------
- Toolbox does not appear after Add Toolbox:
    In the Catalog pane, right-click the folder -> Refresh.

- "DLL load failed" / tool will not load:
    The files were not unblocked (see STEP 1), or your ArcGIS
    Pro is older than 3.2 (different Python version). For an
    older Pro, the .pyd must be rebuilt on that machine.

- The tool/file disappears, or is quarantined:
    Your antivirus/endpoint security removed it. Ask IT to add
    a folder exclusion for where you extracted the tool.

- No API key error:
    Run "jGIS BOX: Configure Claude" first and enter your key.


LICENSE (free distribution)
---------------------------
jGIS BOX is provided FREE of charge. You may use and share it
as-is, at no cost.

IT IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED. The author is NOT liable for any data loss, damage, or
other consequences arising from its use. You use it at your own
risk - keep backups and verify results.

You are responsible for:
  - your own API key and any usage costs charged by the AI
    provider (Anthropic or OpenAI);
  - complying with the AI provider's usage policies and with
    your organization's data-handling rules.

Trademarks belong to their owners. "ArcGIS" is a trademark of
Esri; this product is not affiliated with or endorsed by Esri.

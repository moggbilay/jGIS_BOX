===========================================================================
 jGIS BOX  -  AI agent toolbox for ArcGIS Pro
===========================================================================

 jGIS BOX adds an AI assistant to ArcGIS Pro that can read and control your
 ACTIVE MAP with natural language. You chat with it in plain English and it
 writes and runs arcpy code in your live session - selecting, editing,
 analysing, and adding result layers for you.

 Powered by your choice of provider:
   - Claude  (Anthropic)
   - Codex   (OpenAI)


---------------------------------------------------------------------------
 WHAT'S IN THIS FOLDER
---------------------------------------------------------------------------

   jGISBox.pyt        The toolbox you add to ArcGIS Pro.
   jgisbox_core.pyd   The compiled engine (loads automatically).
   README.txt         This file.

 Keep both jGISBox.pyt and jgisbox_core.pyd together in the same folder.


---------------------------------------------------------------------------
 REQUIREMENTS
---------------------------------------------------------------------------

   - ArcGIS Pro 3.0 or newer (3.0 through 3.6+ are all supported).
   - An API key from your chosen provider:
       Claude  ->  https://console.anthropic.com/
       OpenAI  ->  https://platform.openai.com/api-keys


---------------------------------------------------------------------------
 INSTALL  (READ THE FIRST STEP - IT'S THE #1 CAUSE OF "WON'T LOAD")
---------------------------------------------------------------------------

 1. UNBLOCK FIRST. If you downloaded this as a .zip, Windows marks it as
    untrusted and will refuse to load the compiled .pyd - the toolbox then
    "adds but won't run".

       Right-click the downloaded .ZIP  ->  Properties  ->
       tick  [x] Unblock  (bottom-right)  ->  OK

    Do this BEFORE extracting. It clears the flag on every file inside.

    (Already extracted? Run this once in PowerShell against the folder:
        Get-ChildItem "C:\path\to\folder" -Recurse | Unblock-File   )

 2. Extract the whole folder to a permanent location, e.g.
        C:\Users\<you>\Documents\ArcTools\

 3. In ArcGIS Pro:  Catalog pane  ->  Toolboxes  ->  right-click  ->
        Add Toolbox  ->  browse to  jGISBox.pyt

 4. Expand "jGIS BOX". You'll see three tools (below).


---------------------------------------------------------------------------
 THE TOOLS
---------------------------------------------------------------------------

   jGIS BOX: Configure Claude
       Set your Claude (Anthropic) API key and model. Running this makes
       Claude the active provider for Chat.

   jGIS BOX: Configure Codex
       Set your Codex (OpenAI) API key and model. Running this makes Codex
       the active provider for Chat.

   jGIS BOX: Chat
       Opens the AI chat window. Type what you want in plain language and
       the agent controls your active map. Close the chat window to finish.

 First time: run Configure Claude OR Configure Codex once to set your key,
 then run Chat.


---------------------------------------------------------------------------
 SESSION RULES (standing instructions for every Chat)
---------------------------------------------------------------------------

 In Configure Claude / Configure Codex there is a "Session rules" field.
 Whatever you put there is sent to the AI at the start of EVERY Chat, so you
 don't have to paste your conventions each time. Examples:

     - Prefix all AI-created outputs with AI_
     - Always require an explicit workspace path before creating data
     - Never delete features without asking me first

 Notes:
   - Rules ADD TO the built-in safety rules; they cannot switch safety off.
   - They apply to whichever provider (Claude or Codex) is active - the field
     is shared.
   - Changes take effect on the NEXT Chat you open (rules are read once when a
     Chat starts). The Chat window shows "Session rules active" when they are on.
   - The tool's text box is a single line. For long, multi-line rules, edit the
     "session_rules" value directly in:
         %USERPROFILE%\.arcgis_ai_agent\config.json
   - Rules are capped at ~8000 characters (they are re-sent every message, so
     keep them concise to control token cost).


---------------------------------------------------------------------------
 IMPORTANT - SAFETY
---------------------------------------------------------------------------

   - Chat runs AI-generated arcpy code against your LIVE map. The agent can
     read, edit, and DELETE data. Keep backups of important data and verify
     critical results - the AI can make mistakes.

   - While a step runs, ArcGIS Pro FREEZES ("Not Responding") until that
     step finishes. Heavy geoprocessing on large data may take minutes.
     This is normal, not a crash.

   - For risky or large tasks, turn OFF "Auto-run steps" in the chat window
     so you approve each step. Ask for a count or a small subset before
     running on a whole large dataset.


---------------------------------------------------------------------------
 TROUBLESHOOTING
---------------------------------------------------------------------------

 "Tool won't open / can't import jgisbox_core / cannot load"
   -> 99% of the time this is the download block. Go back to INSTALL step 1
      and Unblock, then re-add the toolbox. Also make sure jgisbox_core.pyd
      is in the SAME folder as jGISBox.pyt (don't run from inside the zip).

 "This ArcGIS Pro runs Python X ... needs a binary ending in ..."
   -> You have an unusually old ArcGIS Pro (before 3.0 / Python 3.9).
      Please update ArcGIS Pro.


===========================================================================
 One file works on every ArcGIS Pro 3.x - no per-version installs.
===========================================================================

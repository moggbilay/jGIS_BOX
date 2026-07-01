import os
import sys

# Keep the toolbox folder clean. ArcGIS Pro and Python drop two kinds of files
# next to this .pyt: bytecode caches (__pycache__) and metadata sidecars
# (*.pyt.xml). We redirect the bytecode cache to the app-data dir and, on every
# load, move any stray __pycache__ / *.pyt.xml into ~/.arcgis_ai_agent so they
# don't accumulate beside the toolbox. All wrapped so it can never block loading.
try:
    _APP_DIR = os.path.join(os.path.expanduser("~"), ".arcgis_ai_agent")
    _META_DIR = os.path.join(_APP_DIR, "toolbox_meta")
    os.makedirs(_META_DIR, exist_ok=True)

    sys.pycache_prefix = os.path.join(_APP_DIR, "pycache")
    sys.dont_write_bytecode = True

    import glob
    import shutil
    _here = os.path.dirname(os.path.abspath(__file__))

    _pc = os.path.join(_here, "__pycache__")
    if os.path.isdir(_pc):
        shutil.rmtree(_pc, ignore_errors=True)

    for _xml in glob.glob(os.path.join(_here, "*.pyt.xml")):
        try:
            _dst = os.path.join(_META_DIR, os.path.basename(_xml))
            if os.path.exists(_dst):
                os.remove(_dst)
            shutil.move(_xml, _dst)
        except Exception:
            pass
except Exception:
    pass

sys.path.insert(0, os.path.dirname(__file__))

from jgisbox_core import Toolbox, ConfigureClaude, ConfigureCodex, ChatTool  # noqa: F401

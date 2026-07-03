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

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# The core is shipped as a compiled binary (jgisbox_core.<abi>.pyd). A given
# .pyd only loads on the exact Python version it was built for, which is tied to
# the ArcGIS Pro version. If this machine's Pro version isn't covered by one of
# the bundled binaries, the import fails - so translate that into a clear,
# actionable message instead of a cryptic "cannot import jgisbox_core".
try:
    from jgisbox_core import Toolbox, ConfigureClaude, ConfigureCodex, ChatTool  # noqa: F401
except ImportError as _err:
    import glob as _glob
    import sysconfig as _sysconfig

    _folder = os.path.dirname(os.path.abspath(__file__))
    _needed_suffix = _sysconfig.get_config_var("EXT_SUFFIX") or "(unknown)"
    _pyver = "%d.%d.%d" % sys.version_info[:3]
    _present = sorted(
        os.path.basename(p)
        for p in _glob.glob(os.path.join(_folder, "jgisbox_core*.pyd"))
    )
    raise ImportError(
        "jGIS BOX could not load its compiled core on this machine.\n"
        "  This ArcGIS Pro runs Python %s, which needs a binary ending in "
        "'%s'.\n"
        "  Binaries bundled in the toolbox folder: %s\n"
        "  Fix: build a copy of jgisbox_core for Python %s (run build.bat on a "
        "machine with this same ArcGIS Pro version) and drop the resulting "
        ".pyd next to jGISBox.pyt.\n"
        "  Original error: %s"
        % (
            _pyver,
            _needed_suffix,
            (", ".join(_present) if _present else "none found"),
            "%d.%d" % sys.version_info[:2],
            _err,
        )
    ) from _err

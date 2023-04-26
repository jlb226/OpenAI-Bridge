if "bpy" in locals():
    import importlib
    # pylint: disable=E0601
    importlib.reload(audio_recorder)
    importlib.reload(pip)
    importlib.reload(common)
    importlib.reload(error_storage)
    importlib.reload(threading)
else:
    from . import audio_recorder
    from . import pip
    from . import common
    from . import error_storage
    from . import threading

# pylint: disable=C0413
import bpy


def register():
    threading.RequestHandler.start()


def unregister():
    threading.RequestHandler.stop()

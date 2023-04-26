bl_info = {
    "name": "OpenAI Bridge",
    "author": "nutti",
    "version": (0, 2, 0),
    "blender": (3, 5, 0),
    "location": "3D View",
    "warning": "",
    "description": "Bridge between Blender and OpenAI",
    "doc_url": "",
    "tracker_url": "",
    "category": "System",
}


if "bpy" in locals():
    import importlib
    # pylint: disable=E0601
    importlib.reload(op)
    importlib.reload(properties)
    importlib.reload(preferences)
    importlib.reload(ui)
    importlib.reload(utils)
else:
    import bpy
    from . import op
    from . import properties
    from . import preferences
    from . import ui
    from . import utils

# pylint: disable=C0413
import bpy


def menu_func(self, context):
    sc = context.scene
    layout = self.layout
    icon_collection = sc.openai_icon_collection["openai_base"]

    layout.separator()
    layout.operator(op.chat.OPENAI_OT_Ask.bl_idname,
                    icon_value=icon_collection.icon_id)
    layout.operator(op.code.OPENAI_OT_GenerateCodeExample.bl_idname,
                    icon_value=icon_collection.icon_id)


def register():
    properties.register_properties()

    op.register()
    bpy.utils.register_class(preferences.OPENAI_OT_EnableAudioInput)
    bpy.utils.register_class(preferences.OPENAI_Preferences)
    ui.register()

    bpy.utils.register_class(utils.threading.OPENAI_OT_ProcessMessage)
    utils.threading.RequestHandler.start()

    bpy.types.WM_MT_button_context.append(menu_func)


def unregister():

    bpy.types.WM_MT_button_context.remove(menu_func)

    bpy.utils.unregister_class(utils.threading.OPENAI_OT_ProcessMessage)
    utils.threading.RequestHandler.stop()

    ui.unregister()
    bpy.utils.unregister_class(preferences.OPENAI_Preferences)
    bpy.utils.unregister_class(preferences.OPENAI_OT_EnableAudioInput)
    op.unregister()

    properties.unregister_properties()

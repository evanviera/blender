import bpy

# Iterate through all scenes in the blend file
for scene in bpy.data.scenes:
    # Set the active scene to the current scene
    bpy.context.window.scene = scene
    # Export the scene as a separate file
    bpy.ops.export_scene.obj(filepath=scene.name + ".obj")

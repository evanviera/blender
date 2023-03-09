# Define information about the add-on
bl_info = {
    "name": "Stamp Text",
    "description": "Adds user-defined text to the render stamp note",
    "author": "Evan Viera",
    "version": (0, 1),
    "blender": (2, 80, 0),
    "location": "Render > Stamp Note Text",
    "category": "Render"
}

# Import Blender Python module
import bpy

# Define a property group for the user-defined text
class StampNoteProperties(bpy.types.PropertyGroup):
    stamp_note_text: bpy.props.StringProperty(
        name="Stamp Note Text", description="Text to be added to the render stamp note")

# Define an operator to add the user-defined text to the stamp note
class AddStampNoteTextOperator(bpy.types.Operator):
    bl_idname = "render.add_stamp_note_text"
    bl_label = "Add Stamp Note Text"
    bl_description = "Adds user-defined text to the render stamp note"

    # Define the execute method for the operator
    def execute(self, context):
        # Get the StampNoteProperties object from the scene
        stamp_note_props = context.scene.stamp_note_props
        # Get the current scene
        scene = context.scene

        # Add the user-defined text to the stamp note
        scene.render.stamp_note_text = stamp_note_props.stamp_note_text
        scene.render.stamp_note_text += " - Beat: "
        scene.render.stamp_note_text += str(bpy.context.scene.frame_current)

        return {'FINISHED'}

# Define a panel to display the user interface for the add-on
class StampNotePanel(bpy.types.Panel):
    bl_idname = "RENDER_PT_StampNote"
    bl_label = "Stamp Note Text"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "render"

    # Define the draw method for the panel
    def draw(self, context):
        layout = self.layout

        # Get the StampNoteProperties object from the scene
        stamp_note_props = context.scene.stamp_note_props

        # Add a property field for the user-defined text
        layout.prop(stamp_note_props, "stamp_note_text")
        # Add a button to add the user-defined text to the stamp note
        layout.operator("render.add_stamp_note_text")

        # Add an "Initialize" button to disable metadata for the output properties of the current scene
        layout.operator("render.initialize", text="Initialize", icon='PLUGIN')

# Define an operator to initialize the stamp note and disable metadata for the output properties of the current scene
class InitializeOperator(bpy.types.Operator):
    bl_idname = "render.initialize"
    bl_label = "Initialize"
    bl_description = "Disable all metadata for the output properties of the current scene"

    # Define the execute method for the operator
    def execute(self, context):
        scene = context.scene

        # Enable the handler so the text updates every time a frame is changed
        bpy.app.handlers.frame_change_post.append(update_stamp_note_text)

        # Disable all metadata for the output properties of the current scene
        scene.render.use_stamp_date = False
        scene.render.use_stamp_time = False
        scene.render.use_stamp_render_time = False
        scene.render.use_stamp_frame = False
        scene.render.use_stamp_frame_range = False
        scene.render.use_stamp_memory = False
        scene.render.use_stamp_hostname = False
        scene.render.use_stamp_camera = False
        scene.render.use_stamp_lens = False
        scene.render.use_stamp_scene = False
        scene.render.use_stamp_marker = False
        scene.render.use_stamp_filename = False
        scene.render.use_stamp_sequencer_strip= False

        # Enable the use of text stamping and set the font size
        scene.render.use_stamp_note = True
        scene.render.use_stamp = True
        scene.render.stamp_font_size = 24
        return {'FINISHED'}


# Define a function that updates the text in the render stamp note
def update_stamp_note_text(scene):
    stamp_note_props = scene.stamp_note_props
    # Set the stamp note text to the value of the property "stamp_note_text"
    scene.render.stamp_note_text = stamp_note_props.stamp_note_text
    # Append the current frame number to the stamp note text
    scene.render.stamp_note_text += " - Beat: "
    scene.render.stamp_note_text += str(scene.frame_current)

# Define the register function
def register():
    # Register the StampNoteProperties class
    bpy.utils.register_class(StampNoteProperties)
    # Create a pointer property "stamp_note_props" in the Scene type, which points to the StampNoteProperties class
    bpy.types.Scene.stamp_note_props = bpy.props.PointerProperty(type=StampNoteProperties)
    # Register the AddStampNoteTextOperator class
    bpy.utils.register_class(AddStampNoteTextOperator)
    # Register the StampNotePanel class
    bpy.utils.register_class(StampNotePanel)
    # Register the InitializeOperator class
    bpy.utils.register_class(InitializeOperator)
    # Append the update_stamp_note_text function to the frame_change_post handler
    bpy.app.handlers.frame_change_post.append(update_stamp_note_text)

# Define the unregister function
def unregister():
    # Unregister the StampNoteProperties class
    bpy.utils.unregister_class(StampNoteProperties)
    # Remove the pointer property "stamp_note_props" from the Scene type
    del bpy.types.Scene.stamp_note_props
    # Unregister the AddStampNoteTextOperator class
    bpy.utils.unregister_class(AddStampNoteTextOperator)
    # Unregister the StampNotePanel class
    bpy.utils.unregister_class(StampNotePanel)
    # Unregister the InitializeOperator class
    bpy.utils.unregister_class(InitializeOperator)
    # Remove the update_stamp_note_text function from the frame_change_post handler
    bpy.app.handlers.frame_change_post.remove(update_stamp_note_text)

# If the script is run directly, call the register function
if __name__ == "__main__":
    register()

    
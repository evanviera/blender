import bpy

# Get a list of all the scenes in the current Blender file
scenes = bpy.data.scenes

# Loop through each scene
for scene in scenes:
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
    scene.render.stamp_font_size = 36

# Define a function to set the text stamp note for each scene
def stamp_beats(scene):
    # Create a string for the text stamp note that includes a custom text and the current frame number
    note_text = "SKY_101_01"
    note_text += "_ beat "
    note_text += str(bpy.context.scene.frame_current)
    
    # Set the text stamp note for the current scene to the custom string
    scene.render.stamp_note_text = note_text

# Add the stamp_set function as a handler that runs every time the frame changes
bpy.app.handlers.frame_change_pre.append(stamp_beats)
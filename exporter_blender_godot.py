"""
Batch tool for importing .obj models and exporting .dae models.
This script requires Godot's Collada Exporter.

blender --background --python exporter_blender_godot.py -- input_path output_path
blender --background --python exporter_blender_godot.py -- "../Assets/Nature Kit OBJ/" "../Assets/Nature Kit DAE/"
"""
import sys
import os
import bpy


def run(input_path, output_path):
    """
    Runs the batch tool.

    :param input_path: Input folder with .obj files.
    :param output_path: Output folder for .dae files.
    """

    all_files = sorted(os.listdir(input_path))
    obj_files = [f for f in all_files if f.endswith(".obj")]

    for filename in obj_files:
        input_filepath = os.path.join(input_path, filename)
        output_filepath = os.path.join(output_path, filename.replace(".obj", ".dae"))

        os.makedirs(output_path, exist_ok=True)

        bpy.ops.wm.read_homefile()
        bpy.ops.object.select_all(action="SELECT")
        bpy.ops.object.delete()

        process_file(input_filepath, output_filepath)


def process_file(input_filepath, output_filepath):
    """
    Imports the .obj file and exports as .dae file.

    :param input_filepath: Complete input filepath for .obj model.
    :param output_filepath: Complete output filepath for .dae model.
    """

    # import and select
    bpy.ops.import_scene.obj(
        filepath=input_filepath, use_edges=True, use_smooth_groups=False
    )
    current = bpy.context.selected_objects[0]
    bpy.context.scene.objects.active = current

    # clean shading
    bpy.ops.object.mode_set(mode="OBJECT")
    current.data.use_auto_smooth = 0
    bpy.ops.object.shade_smooth()
    bpy.ops.object.modifier_add(type="EDGE_SPLIT")

    # clean mesh
    bpy.ops.object.mode_set(mode="EDIT")
    bpy.ops.mesh.dissolve_limited()
    bpy.ops.mesh.remove_doubles()
    bpy.ops.mesh.normals_make_consistent(inside=False)

    # export model
    bpy.ops.object.mode_set(mode="OBJECT")
    bpy.ops.export_scene.dae(
        filepath=output_filepath, use_mesh_modifiers=True, use_triangles=True
    )


# run the batch tool
argv = sys.argv
argv = argv[argv.index("--") + 1 :]

run(argv[0], argv[1])

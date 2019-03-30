# Batch Blender-Godot Exporter

Batch tool for importing .obj models and exporting .dae models.

It also cleans the mesh:

- Fix shading with auto smooth, shade smooth and edge split modifier.
- Remove duplicate vertices and recompute normals.
- Export meshes using triangles.

## Usage

This script requires Godot's Collada Exporter (tested using Blender 2.7).

Download the .py script and run it using Blender:

```bash
blender --background --python exporter_blender_godot.py -- input_path output_path

blender --background --python exporter_blender_godot.py -- "../Assets/Nature Kit OBJ/" "../Assets/Nature Kit DAE/"
```

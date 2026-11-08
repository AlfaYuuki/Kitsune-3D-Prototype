"""Generate editable Kitsune 3D anime NPC scenes in Blender.

Run from Blender 3.6+:
  blender --background --python tools/blender/generate_kitsune_npcs.py

Creates one .blend and one .glb per NPC under assets/characters/.
"""
import bpy, math, os
from mathutils import Vector

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(ROOT, "assets", "characters")
os.makedirs(OUT, exist_ok=True)

PALETTE = {
    "skin": (0.96, 0.78, 0.67, 1), "white": (0.96, 0.94, 0.89, 1),
    "hair": (0.08, 0.055, 0.09, 1), "hair2": (0.18, 0.11, 0.16, 1),
    "red": (0.62, 0.055, 0.07, 1), "red2": (0.82, 0.13, 0.15, 1),
    "gold": (0.82, 0.57, 0.19, 1), "green": (0.19, 0.32, 0.24, 1),
    "brown": (0.27, 0.17, 0.11, 1), "purple": (0.26, 0.17, 0.42, 1),
    "orange": (0.8, 0.37, 0.1, 1), "iris": (0.2, 0.48, 0.65, 1),
    "dark": (0.035, 0.025, 0.03, 1), "gray": (0.62, 0.62, 0.67, 1),
    "bead": (0.37, 0.18, 0.09, 1), "straw": (0.72, 0.59, 0.34, 1),
}

def material(name, color):
    m = bpy.data.materials.new(name)
    m.diffuse_color = color
    m.use_nodes = True
    bs = m.node_tree.nodes.get("Principled BSDF")
    bs.inputs["Base Color"].default_value = color
    bs.inputs["Roughness"].default_value = 0.72 if name != "gold" else 0.34
    if name == "gold":
        bs.inputs["Metallic"].default_value = 0.45
    return m

MATS = {k: material(k, v) for k, v in PALETTE.items()}

def finish(obj, name, mat):
    obj.name = name
    obj.data.materials.append(MATS[mat])
    for p in obj.data.polygons:
        p.use_smooth = True
    return obj

def sphere(name, mat, loc, scale):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=16, ring_count=12, location=loc)
    o = bpy.context.object
    o.scale = scale
    return finish(o, name, mat)

def cylinder(name, mat, loc, scale, vertices=16, radius1=1, radius2=1):
    bpy.ops.mesh.primitive_cone_add(vertices=vertices, radius1=radius1, radius2=radius2,
                                   depth=1, location=loc)
    o = bpy.context.object
    o.scale = scale
    return finish(o, name, mat)

def build(kind):
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    if kind == "hinata":
        cylinder("Shrine maiden hakama", "red", (0,.73,0), (.44,.69,.31), radius1=1.0, radius2=.62)
        cylinder("White upper kimono", "white", (0,1.36,0), (.31,.275,.23), radius1=.65, radius2=.55)
        cylinder("Gold obi", "gold", (0,1.13,0), (.46,.05,.33))
        for side in (-1,1):
            cylinder("Wide sleeve", "white", (side*.39,1.24,0), (.115,.31,.135))
            sphere("Hand", "skin", (side*.4,.91,-.02), (.075,.08,.075))
        sphere("Face", "skin", (0,1.96,0), (.29,.32,.26))
        sphere("Hair cap", "hair", (0,2.02,.06), (.315,.335,.29))
        sphere("Hair crown", "hair", (0,2.26,.04), (.275,.18,.27))
        for side in (-1,1):
            sphere("Long side lock", "hair", (side*.29,1.98,-.02), (.09,.19,.10))
            sphere("Hair bun", "hair2", (side*.48,2.1,.02), (.095,.10,.095))
            sphere("Eye white", "white", (side*.115,1.99,-.252), (.052,.06,.022))
            sphere("Blue iris", "iris", (side*.115,1.99,-.292), (.028,.039,.013))
            sphere("Pupil", "dark", (side*.115,1.99,-.312), (.014,.024,.007))
        sphere("Red hair ribbon", "red2", (0,2.42,.02), (.12,.055,.07))
        sphere("Ribbon tail", "red2", (-.18,2.4,.02), (.08,.06,.06))
    elif kind == "genzo":
        cylinder("Brown robe", "brown", (0,.72,0), (.45,.71,.34), radius1=1, radius2=.65)
        cylinder("Green haori", "green", (0,1.35,0), (.36,.29,.29), radius1=.75, radius2=.64)
        cylinder("Gold sash", "gold", (0,1.17,0), (.43,.045,.31))
        sphere("Elder face", "skin", (0,1.97,0), (.285,.305,.26))
        sphere("Silver hair", "gray", (0,2.25,.05), (.30,.16,.275))
        sphere("Long white beard", "white", (0,1.72,-.23), (.135,.17,.14))
        for side in (-1,1):
            sphere("White brow", "gray", (side*.115,1.99,-.25), (.05,.05,.02))
            sphere("Eye", "dark", (side*.115,1.99,-.282), (.015,.02,.01))
        cylinder("Straw hat brim", "straw", (0,2.48,0), (.575,.05,.575))
        cylinder("Hat crown", "brown", (0,2.43,0), (.12,.075,.12))
        cylinder("Walking staff", "brown", (.58,.94,.03), (.035,.95,.035))
        for i in range(9):
            a=i*math.tau/9
            sphere("Prayer bead", "bead", (math.cos(a)*.31,1.55,math.sin(a)*.31), (.028,.028,.028))
    else:
        cylinder("Monk robe", "purple", (0,.73,0), (.45,.71,.34), radius1=1, radius2=.64)
        cylinder("Orange stole", "orange", (0,1.34,0), (.36,.275,.29), radius1=.75, radius2=.64)
        cylinder("Gold belt", "gold", (0,1.16,0), (.425,.04,.31))
        sphere("Face", "skin", (0,1.97,0), (.285,.305,.26))
        sphere("Dark hair", "hair", (0,2.23,.04), (.29,.14,.265))
        for side in (-1,1):
            sphere("Side hair", "hair", (side*.27,1.98,.04), (.09,.12,.09))
            sphere("Eye white", "white", (side*.115,1.99,-.25), (.05,.055,.02))
            sphere("Iris", "iris", (side*.115,1.99,-.28), (.027,.035,.013))
            sphere("Pupil", "dark", (side*.115,1.99,-.30), (.013,.02,.007))
        cylinder("Walking staff", "brown", (-.58,.95,.03), (.03,.975,.03))
        sphere("Staff ornament", "gold", (-.58,1.96,.03), (.065,.06,.065))
        for i in range(11):
            a=i*math.tau/11
            sphere("Prayer bead", "bead", (math.cos(a)*.32,1.53,math.sin(a)*.32), (.023,.023,.023))

    # Keep a simple, clean origin and apply transforms for predictable game scale.
    for obj in bpy.context.scene.objects:
        if obj.type == "MESH":
            bpy.context.view_layer.objects.active = obj
            obj.select_set(True)
            bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
            obj.select_set(False)
    bpy.ops.object.select_all(action="SELECT")
    bpy.context.scene.unit_settings.system = "METRIC"
    bpy.context.scene.render.engine = "BLENDER_EEVEE_NEXT"
    bpy.ops.wm.save_as_mainfile(filepath=os.path.join(OUT, kind + ".blend"))
    bpy.ops.export_scene.gltf(filepath=os.path.join(OUT, kind + ".glb"),
                              export_format="GLB", export_apply=True,
                              export_materials="EXPORT", export_yup=True)
    print("Created", kind, "Blender scene and GLB")

for character in ("hinata", "genzo", "sora"):
    build(character)

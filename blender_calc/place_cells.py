import math
import mathutils
import numpy as np
import bpy
import bmesh
from math import sqrt

def get_distance():
    """
    return: float. Distance of the two objects
    Must select two objects
    """
    l = []  # we store the loacation vector of each object
    for item in bpy.context.selected_objects:
        l.append(item.location)

    distance = sqrt( (l[0][0] - l[1][0])**2 + (l[0][1] - l[1][1])**2 + (l[0][2] - l[1][2])**2)
    print(distance)  # print distance to console, DEBUG
    return distance

def creer_pile(x, y):
    bpy.ops.object.select_by_type(type='EMPTY')
    object = bpy.data.objects['18650 Battery.000']
    object.select = True
    bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, \
TRANSFORM_OT_translate={"value":(x, y, 0), "constraint_axis":(False, False, False), \
"constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', \
"proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, \
"snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, \
"release_confirm":False})
    print(x, y)


left_wall = bpy.ops.mesh.primitive_plane_add(view_align=False, enter_editmode=False, location=(0, 0, 0), rotation=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
bpy.ops.rigidbody.objects_add(type='PASSIVE')
bpy.context.scene.cursor_location = (1.0, 0.0, 0.0)
bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
bpy.context.object.location[0] = 0
bpy.context.object.rotation_euler[1] = 0.7
bpy.context.object.scale[1] = 4


right_wall = bpy.ops.mesh.primitive_plane_add(view_align=False, enter_editmode=False, location=(0, 0, 0), rotation=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
bpy.ops.rigidbody.objects_add(type='PASSIVE')
bpy.context.scene.cursor_location = (1.0, 0.0, 0.0)
bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
bpy.context.object.location[0] = 0
bpy.context.object.rotation_euler[1] = math.pi - 0.8
bpy.context.object.scale[1] = 4

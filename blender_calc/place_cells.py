import math
import mathutils
import numpy as np
import bpy
import bmesh
from math import sqrt
import time

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

def create_cell(x, y, z, i = 1):
    # select the model of the cell
    bpy.ops.object.select_by_type(type='EMPTY')
    object = bpy.data.objects['18650 Battery.000']
    object.select = True
    # copy object
    object2 = bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, \
TRANSFORM_OT_translate={"value":(0, 0, 0), "constraint_axis":(False, False, False), \
"constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', \
"proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, \
"snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, \
"release_confirm":False})
    # rotate it
    id_ = "0" * (3 - len(str(i))) + str(i)
    obj_name = '18650 Battery.' + id_
    bpy.data.objects[obj_name].rotation_euler[0] = 3 * math.pi / 2
    bpy.data.objects[obj_name].location[0] = x
    bpy.data.objects[obj_name].location[1] = y
    bpy.data.objects[obj_name].location[2] = z
    # we position the origin of the object at the center of mass, so that the animation is realistic
    bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')
    bpy.ops.rigidbody.objects_add(type='ACTIVE')


width = 4

# we create the left wall
l_left = 10
left_wall = bpy.ops.mesh.primitive_plane_add(view_align=False, enter_editmode=False, location=(0, 0, 0), rotation=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
# set the behaviour for the animation
bpy.ops.rigidbody.objects_add(type='PASSIVE')
# set the cursor location (= origin of the object)
bpy.context.scene.cursor_location = (1.0, 1.0, 0.0)
bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
# place the object
bpy.context.object.location[0] = 0
bpy.context.object.rotation_euler[1] = 0.7
bpy.context.object.scale[0] = l_left
bpy.context.object.scale[1] = width

# we create the right wall
l_right = 15
right_wall = bpy.ops.mesh.primitive_plane_add(view_align=False, enter_editmode=False, location=(0, 0, 0), rotation=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
bpy.ops.rigidbody.objects_add(type='PASSIVE')
bpy.context.scene.cursor_location = (1.0, 1.0, 0.0)
bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
bpy.context.object.location[0] = 0
bpy.context.object.rotation_euler[1] = math.pi - 0.8
bpy.context.object.scale[0] = l_right
bpy.context.object.scale[1] = width

# we create the cells
# first one in the bottom
create_cell(0, 0, 2, 1)
# the 2 of the second row
create_cell(-1.5, 0, 3, 2)
create_cell(1.5, 0, 3, 3)
# the 3 of the third row
create_cell(-2.5, 0, 4.5, 4)
create_cell(0, 0, 4.5, 5)
create_cell(2.5, 0, 4.5, 6)

# we play the animation
i = 0
while i < 70:
     #go to next frame
     bpy.context.scene.frame_set(bpy.context.scene.frame_current + 1)
     i += 1

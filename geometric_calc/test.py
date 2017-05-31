import math
import mathutils
import numpy as np
import bpy

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

R=1.82/2
hauteur = 6.515
dx=R
dy=2*R*np.cos(np.pi/6)
nb_etages = 6
print("===============")

for i in range(2, nb_etages):
    print("ligne " + str(i))
    x1 = 0 - (i - 1) * dx
    y1 = 0 + (i - 1) * dy
    creer_pile(x1, y1)
    
    for j in range(2, i + 1):
        print("colonne " + str(j))
        x = x1 + 2 * R * (j - 1)
        y = y1
        creer_pile(x, y)


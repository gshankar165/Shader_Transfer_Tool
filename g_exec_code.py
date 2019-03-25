'''
g_exec_code.py

This file has been linked with 4 files.
g_common_funcs.py,  g_logic_funcs.py, g_ui_file.py, __init__.py

make sure if you keep these 4 files inside gCommon_scripts folder
under the main directory before execute the script.

Now replace the path of main directory as per your os windows/linux/mac= "directory path here"

execute the script in Maya-Python script editor.

Software: Maya (support version 2017, 2018, 2019)
It supports Centos, windows, Mac. I have not checked with red_hat linux yet.


How it Works:
1. suppose there is a lookdev completed char group or group of meshes in maya scene.
you got rig/model updated char group from the other dep and you need to re assign
2. shaders and mesh attributes (opaque, subdivisions).
3. This tool will do all these work in seconds.
4. Keep both old asset group and new in the scene.
5. just select old meshes (not group, only mesh ) which has shaders, run the script.

Limitations:
1. Both the old and new char/objects must have same mesh naming and follow proper naming convention.
2. For Mesh Attribute copy, current I have implemented for Arnold.
 (opaque, subdivision type and iteration, UV smoothing in shape node)
3. For other renderers support, available on request.

images are avilable here: https://knowledge.autodesk.com/community/article/230446

----Author-----
Girijashankar Senapati
gshankar165@gmail.com

'''



import sys
import os
import maya.cmds as cmds

# replace windows path here. Do not remove *r before quotation
windows_path= "r"+'"E:\Code_test\Shader_Transfer_Tool"'

# if linux, replace the path here.11
linux_path=    "/home/gssLinux/PycharmProjects/Shader_Transfer_Tool"

platform= sys.platform

if "linux" in platform:
    sys.path.append(linux_path)
elif "darwin" in platform:
    sys.path.append(linux_path)
else:
    sys.path.append(windows_path)


from gCommon_scripts.g_common_funcs import gCommonFuncs
from gCommon_scripts.g_common_funcs import gConnectFunc
from gCommon_scripts.g_logic_funcs import *
from gCommon_scripts.g_ui_file import *


print main_window()

# Shader_Transfer_Tool

Licensing: 
This is a free tool for commercial and non commercial use.
User can use it in his personal or company workstation. 
User can upgrade as per his requirements. 

Usuge:
Replace the code_path in g_exec_code.py file and execute file in Maya-Python script editor.
Software: Maya (support version 2017 later)
It supports Centos, windows, Mac. 

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

I would love to see an appreciation mail. 

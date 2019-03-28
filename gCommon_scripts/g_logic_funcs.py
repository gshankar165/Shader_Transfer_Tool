'''
g_logic_funcs.py

file contains the logic functions to run the script.
shader_transfer : copy shaders from selected objects to same naming other objects.
mesh_attrib_transfer: copy mesh attribs from sel objs to same named other objs.

it also return unique objects; unsuccessfull transfers issues objects
incase of unmatched mesh namings.

'''

from g_common_funcs import gCommonFuncs, gConnectFunc


import maya.cmds as cmds


lambert_list=[]     # some initialshadinggroup meshes of selection list
attrib_list=[".aiOpaque", ".aiSubdivType", ".aiSubdivIterations", ".aiSubdivUvSmoothing"]


def shader_transfer():
    '''
    This function runs on selected meshes.
    Once you select meshes, it will query its shape node.
    get shading group, Then shader name.
    store in a variable.
    Then assign to similar naming meshes available in the scene

    :return: array:: lambert shader assigned object
    '''
    global lambert_list

    sel_objects = gCommonFuncs(name=None).get_live_mesh_sel()

    if sel_objects:
        for e_mesh in sel_objects:
            shape_node = gCommonFuncs(name=e_mesh).get_shape_node()  # get the shape node of mesh
            shading_grp = gCommonFuncs(name=shape_node).get_sg_node()  # get the shading grp name of the selected mesh shape node

            if shading_grp:     # run if shading_grp return any shader else add shape_node to no lambert_shader list
                xMaterial = gCommonFuncs(name=shading_grp).get_shader()  # get the shader name shading grp

                g_mesh = e_mesh.split("|")[-1]
                similar_objects = gCommonFuncs(name=g_mesh).sel_similar_mesh()  # select similar meshes by the e_mesh name

                for e_obj in similar_objects:
                    gShape = gCommonFuncs(name=e_obj).get_shape_node()  # get the shape node of last splited string
                    if gShape!=None:
                        for e_shape in gShape:
                            if "Shape" in e_shape:                                
                                    g_node = gCommonFuncs(name=e_shape).get_sg_node()  # get the shading group name of the mesh shape

                                    # match the mesh g_SG shading group to variable shading_grp. if not match, assign the xMaterial to the mesh
                                    if g_node == shading_grp:
                                        None
                                    else:
                                        print e_obj
                                        print xMaterial[0]
                                        gConnectFunc(name=e_obj).shader_assign(xShader=xMaterial[0])  # assign the shader to the new mesh

            else:
                lambert_list.append(shape_node[0])

    else:
        cmds.warning("No meshes selected to assign the shader")

    if len(lambert_list)>0:
        cmds.warning("Some meshes have initialShadingGroup or no Shader assigned, check script editor")
        cmds.warning(" below is the list of those unique meshes; shader assigned failed")
        print lambert_list




def mesh_attrib_transfer(sel_objects):
    '''
    This function runs on selected meshes.
    Once you select meshes, it will query its shape node.
    get the arnold attributes, store in variable.
    Then update to similar naming meshes attributes.
    :return: None
    '''

    live_plugins= cmds.pluginInfo( query=True, listPlugins=True )

    for e_msh in sel_objects:
        shape_node = gCommonFuncs(name=e_msh).get_shape_node()  # get the shape node of mesh
        chk_plugin= gCommonFuncs(name=live_plugins).plugin_chk()     # checking weather the mtoa plugin loaded or not.
        if chk_plugin:
            for e_attrib in attrib_list:
                xAttrib= gConnectFunc(name=shape_node[0]).get_mesh_attrib(attrb=e_attrib)
                g_msh = e_msh.split("|")[-1]
                similar_objects = gCommonFuncs(name=g_msh).sel_similar_mesh()  # select similar meshes by the e_mesh name

                for t_msh in similar_objects:
                    xShape = gCommonFuncs(name=t_msh).get_shape_node() # get the shape node of last splited string
                    zAttrib = gConnectFunc(name=xShape[0]).get_mesh_attrib(attrb=e_attrib)  # get the mesh attribute value4

                    if zAttrib==xAttrib:
                        None
                    else:
                        print xShape[0]+e_attrib
                        print int(xAttrib)
                        print "value changed"
                        gConnectFunc(name=xShape[0]).set_mesh_attrib(attrb=e_attrib, value=int(xAttrib)) # update mesh attrtibuts
        else:
            cmds.warning("Arnold Plugin has not been loaded. Please load and redo the process")

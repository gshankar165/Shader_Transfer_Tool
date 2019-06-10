'''

g_common_funcs.py

file contains all maya functions for running the script.
maya.cmds python command have been used.

TWo main class.
gCommonFuncs, gConnectFunc

'''


import maya.cmds as cmds


class gCommonFuncs(object):
    def __init__(self,name):
        self.name=name

    def plugin_chk(self, name=None):
        '''
        :param name: array:: list of all loaded plugin in maya
        :return: Bool True/ False
        '''
        return bool("mtoa" in str(self.name))

    def get_live_mesh_sel(self):
        '''
        :return: arrey:: list of object(mesh) selections on viewport by user
        '''
        live_objects= cmds.ls(sl=True)
        return live_objects

    def get_shape_node(self, name=None):
        '''
        :return: arrey:: list of object(mesh) selections on viewport by user
        '''
        return cmds.listRelatives(self.name, shapes=True, fullPath=True) or []

    def get_sg_node(self, name=None):
        '''
        :param name: string:: mesh shape node name
        :return: string:: shader name of the given mesh shape
        '''
        conn_list= cmds.listConnections(self.name)
        if conn_list!=None:
            for e_obj in conn_list:
                if "SG" in e_obj:
                    return e_obj
                else:
                    continue

    def get_shader(self, name=None):
        '''
        :param name: string:: shading group name
        :return: string: shader name that connected to shading group
        '''
        if "GroupId" not in self.name:
            exist_shader= cmds.listConnections(self.name+".surfaceShader")
            return exist_shader

    def sel_similar_mesh(self, name=None):
        '''
        :param name: string:: mesh name
        :return: array:: list of meshes which does have *Shape string
        '''
        attrC="*"+self.name
        pre_objs = cmds.ls(attrC)
        return pre_objs

    def attr_exist(self, name=None):
        '''
        :param name: string:: mesh name
        :return: array:: list of attributes exist in shape node
        '''
        return cmds.attributeMenu(self.name)

class gConnectFunc(gCommonFuncs):
    '''
    main function to assign shader to mesh
    '''


    def shader_assign(self, name=None, xShader=None):
        '''

        :param name: string:: mesh name
        :param xShader: string:: shader name
        :return: None
        '''
        cmds.select(self.name)
        cmds.hyperShade(assign= xShader)   # assign the shader to the mesh


    def get_mesh_attrib(self, name=None, attrb=None):
        '''
        :param name: string:: mesh name
        :param attrib: string:: attribute name to copy
        :return: string:: Bool:: int:: float:: values
        '''
        return cmds.getAttr(self.name + attrb)

    def set_mesh_attrib(self, name=None, attrb=None, value=None):
        '''
        :param name: string:: mesh name
        :param attrib: string:: attribute name to copy
        :param value: string:: attribute name to copy
        :return: None
        '''
        return cmds.setAttr(self.name + attrb, value)

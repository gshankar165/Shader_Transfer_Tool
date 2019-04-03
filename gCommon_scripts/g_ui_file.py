'''

g_ui_file.py
this is the ui file of the project.
maya_python ui file.

'''

from g_common_funcs import gCommonFuncs
from g_logic_funcs import shader_transfer, mesh_attrib_transfer

import maya.cmds as cmds


def shader_transfer_btn(*arg):
    '''
    ui transfer button command
    :return: array:: list of selected meshes.
    '''
    global sel_objects
    sel_objects = gCommonFuncs(name=None).get_live_mesh_sel()
    shader_transfer()
    cmds.confirmDialog(title='Shader Transfer Done', message='Process has been completed. Please check script editor for Errors!! ', defaultButton='Yes')
    return sel_objects

def mesh_attrib_transfer_btn(*arg):
    '''
    ui transfer button command
    :return: None
    '''
    sel_objects=gCommonFuncs(name=None).get_live_mesh_sel()
    mesh_attrib_transfer(sel_objects)
    cmds.confirmDialog(title='Mesh Attribute Transfer Done', message='Process has been completed ', defaultButton='Yes')


def main_window():
    cmds.window("Shader_Transfer_Tool_v1.0", width=230, height=21)

    cmds.columnLayout(columnAttach=('both', 5), rowSpacing=10, columnWidth=300)
    cmds.text(label='   ', align="left")
    cmds.text(label='Select only old meshes and Click', align="left")
    cmds.button(label="Shader Transfer", command=(shader_transfer_btn))
    cmds.button(label="Mesh Attrib Transfer", command=(mesh_attrib_transfer_btn))

    cmds.columnLayout(columnAttach=('both', 5), rowSpacing=2, columnWidth=250)
    cmds.text(label='   ', align="right")
    cmds.text(label='   ', align="right")
    cmds.text(label='--Author', align="right")
    cmds.text(label='Girijashankar Senapati', align="right")
    cmds.text(label='gshankar165@gmail.com', align="right")

    cmds.showWindow()

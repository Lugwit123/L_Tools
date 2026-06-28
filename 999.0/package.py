# -*- coding: utf-8 -*-

name = "L_Tools"
version = "999.0"
description = "Lugwit system tools - window management, admin utilities"
authors = ["Lugwit Team"]

requires = ["python-3.12+<3.13", "pyside6", "Lugwit_Module", "pywin32", "qtpy", "l_qt_wgt_lib"]

build_command = False
cachable = True
relocatable = True

def commands():
    import os
    # sys_tool 目录下的模块直接可 import（l_window, l_admin, l_window_control 等）
    env.PYTHONPATH.prepend("{root}/sys_tool")
    env.L_TOOLS_ROOT = "{root}"
    alias("set_disk_link", "python {root}/sys_tool/setDiskLink/setDiskLink.py")
    alias("set_env_var", "python {root}/sys_tool/setEnvVar.py")

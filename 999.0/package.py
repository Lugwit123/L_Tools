# -*- coding: utf-8 -*-

name = "L_Tools"
version = "999.0"
description = "Lugwit system tools - window management, admin utilities"
authors = ["Lugwit Team"]

requires = ["python-3.12+<3.13"]

build_command = False
cachable = True
relocatable = True

def commands():
    import os
    # sys_tool 目录下的模块直接可 import（l_window, l_admin, l_window_control 等）
    env.PYTHONPATH.prepend("{root}/sys_tool")
    env.L_TOOLS_ROOT = "{root}"

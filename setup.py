__author__ = 'nrot'

# -*- coding: utf-8 -*-

import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os", "random", "glob", "shutil", "xml", "lxml"], "optimize": 1,
                     "include_files": ["OriginFile.xml"]}

setup(
    name="NewFons",
    version="1.1b",
    author=__author__,
    description='Download random image from same site',
    options={"NewFons_exe": build_exe_options},
    executables=[Executable("Main.py", base="Console")]
)
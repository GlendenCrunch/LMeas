#!/usr/bin/python3-32
# -*- coding: utf-8 -*-
import sys
from cx_Freeze import setup, Executable

sys.argv.append("build")
setup(
    name = "LMeas",
    version = "2.0",
    description = "LMeas",
    author = "ITL",
    executables = [Executable(script = "LMeas.py", icon="icon/icon.ico", base="Win32GUI")] #Win32GUI-выключает консоль
)

#!/usr/bin/python3-32
# -*- coding: utf-8 -*-
import subprocess

subprocess.call(r'python -m PyInstaller --onefile --icon=icon/icon.ico --console --name LMeas C:\ITL\LCARD\LMeas.py')

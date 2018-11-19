# -*- coding: utf-8 -*-
import sys
import os
import subprocess
cwd = os.getcwd()
os.chdir(os.path.join(cwd, "App/qmlview/qmlview"))
"""out = subprocess.check_output(['qml_preview',
                               "C:/Users/GODWIN/Documents/GitHub/Ninja-Preview/main.qml",
                               "-style",
                               "material"])"""
stat = ['qmlview',
        "C:/Users/GODWIN/Documents/GitHub/Ninja-Preview/UI/main.qml"]
if len(sys.argv) > 2:
    stat.extend(sys.argv[1:])
print(stat)
out = subprocess.check_output(stat, shell=True)
print(out)


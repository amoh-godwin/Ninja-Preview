# -*- coding: utf-8 -*-
# Thank you My Father
import sys
import os
from PyQt5.QtGui import QGuiApplication, QIcon
from PyQt5.QtQml import QQmlApplicationEngine
from preview import Preview

def run():
    engine.load('UI/main.qml')

qApp = QGuiApplication(sys.argv)
qApp.setWindowIcon(QIcon("/UI/icons/logo.ico"))

engine = QQmlApplicationEngine()
preview = Preview()
engine.rootContext().setContextProperty('preview', preview)
os.chdir('C:\\Users\\GODWIN\\Documents\\GitHub\\Ninja-Preview')
run()
cwd = os.getcwd()
os.chdir(os.path.join(cwd, "App/qmlview/qmlview"))
engine.quit.connect(qApp.quit)

#qApp.aboutToQuit.connect(self._postprocess)
qApp.exec_()

sys.exit()
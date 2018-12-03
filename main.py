# -*- coding: utf-8 -*-
import sys
import os
from PyQt5.QtGui import QGuiApplication, QIcon
from PyQt5.QtQml import QQmlApplicationEngine
from preview import Preview


def cleanUp():
    print(preview.app_closed)
    preview.app_closed = True
    print('\n', preview.app_closed)
    return


qApp = QGuiApplication(sys.argv)

qApp.setWindowIcon(QIcon("/UI/icons/logo.ico"))

engine = QQmlApplicationEngine()
preview = Preview()
engine.rootContext().setContextProperty('preview', preview)

os.chdir('C:\\Users\\GODWIN\\Documents\\GitHub\\Ninja-Preview')

engine.load('UI/main.qml')

cwd = os.getcwd()
os.chdir(os.path.join(cwd, "App/qmlview/qmlview"))

engine.quit.connect(qApp.quit)

qApp.aboutToQuit.connect(cleanUp)
qApp.exec_()

sys.exit()

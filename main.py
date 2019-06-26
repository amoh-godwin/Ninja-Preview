# -*- coding: utf-8 -*-
import sys
from PyQt5.QtGui import QGuiApplication, QIcon
from PyQt5.QtQml import QQmlApplicationEngine
from preview import Preview


def cleanUp():
    print(preview.app_closed)
    preview.app_closed = True
    print('\n', preview.app_closed)
    return


qApp = QGuiApplication(sys.argv)

qApp.setWindowIcon(QIcon("/UI/icons/logo.png"))

engine = QQmlApplicationEngine()
preview = Preview()
engine.rootContext().setContextProperty('preview', preview)

engine.load('UI/main.qml')

engine.quit.connect(qApp.quit)

qApp.aboutToQuit.connect(cleanUp)
qApp.exec_()

sys.exit()

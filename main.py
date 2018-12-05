# -*- coding: utf-8 -*-
import sys
from PyQt5.QtGui import QGuiApplication, QIcon
from PyQt5.QtQml import QQmlApplicationEngine
from preview import Preview


def cleanUp():
    preview.app_closed = True
    return


qApp = QGuiApplication(sys.argv)

qApp.setWindowIcon(QIcon("./UI/icons/logo.ico"))

engine = QQmlApplicationEngine()

preview = Preview()

engine.rootContext().setContextProperty('preview', preview)

engine.load('UI/main.qml')

engine.quit.connect(qApp.quit)

qApp.aboutToQuit.connect(cleanUp)

sys.exit(qApp.exec_())

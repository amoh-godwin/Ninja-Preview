# -*- coding: utf-8 -*-
import sys
import os
from base64 import b64decode
from PyQt5.QtCore import QCoreApplication, QSettings, QResource
from PyQt5.QtGui import QGuiApplication, QIcon
from PyQt5.QtQml import QQmlApplicationEngine
from Ninja_Preview.preview import Preview
from Ninja_Preview._ninjapreview_resource import rcc

def dummy_run():
    pass


dec = b64decode(rcc)

with open('_ninjapreview_resource.rcc', 'wb') as rcc_f:
    rcc_f.write(dec)

QResource.registerResource("_ninjapreview_resource.rcc")

qApp = QGuiApplication(sys.argv)

QCoreApplication.setOrganizationName("Deuteronomy Works")
QCoreApplication.setApplicationName("Ninja-Preview")
settings = QSettings()

qApp.setWindowIcon(QIcon(":icons/logo.png"))

engine = QQmlApplicationEngine()

preview = Preview()

engine.rootContext().setContextProperty('preview', preview)

engine.load("qrc:///UI/main.qml")

engine.quit.connect(qApp.quit)

sys.exit(qApp.exec_())

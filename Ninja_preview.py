# -*- coding: utf-8 -*-
import sys
import os

from PyQt6.QtCore import QCoreApplication, QSettings, QResource
from PyQt6.QtGui import QGuiApplication, QIcon
from PyQt6.QtQml import QQmlApplicationEngine

from preview import Preview


QResource.registerResource("_ninjapreview_resource.rcc")

qApp = QGuiApplication(sys.argv)

QCoreApplication.setOrganizationName("Deuteronomy Works")
QCoreApplication.setApplicationName("Ninja-Preview")
settings = QSettings()

qApp.setWindowIcon(QIcon(":icons/logo.png"))

engine = QQmlApplicationEngine()

preview = Preview()

engine.load("qrc:///UI/main.qml")
engine.rootObjects()[0].setProperty('preview', preview)
engine.quit.connect(qApp.quit)

sys.exit(qApp.exec())

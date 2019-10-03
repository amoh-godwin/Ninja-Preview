# -*- coding: utf-8 -*-
import sys
import os
from PyQt5.QtCore import QCoreApplication, QSettings, QResource
from PyQt5.QtGui import QGuiApplication, QIcon
from PyQt5.QtQml import QQmlApplicationEngine
from preview import Preview

qApp = QGuiApplication(sys.argv)

QCoreApplication.setOrganizationName("Deuteronomy Works")
QCoreApplication.setApplicationName("Ninja-Preview")
settings = QSettings()

QResource.registerResource('resource.rcc')

qApp.setWindowIcon(QIcon(":icons/logo.png"))

engine = QQmlApplicationEngine()

preview = Preview()

engine.rootContext().setContextProperty('preview', preview)

engine.load('qrc:///UI/main.qml')

engine.quit.connect(qApp.quit)

sys.exit(qApp.exec_())

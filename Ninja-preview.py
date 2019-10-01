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

QResource.registerResource('resources.rcc')

qApp.setWindowIcon(QIcon(":/UI/icons/logo.ico"))

engine = QQmlApplicationEngine()

preview = Preview()

engine.rootContext().setContextProperty('preview', preview)

engine.load('qrc:///UI/main.qml')

cwd = os.getcwd()
os.chdir(os.path.join(cwd, "App/qmlview"))
engine.quit.connect(qApp.quit)

sys.exit(qApp.exec_())

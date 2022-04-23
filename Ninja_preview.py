# -*- coding: utf-8 -*-
import sys
import os

from PyQt6.QtCore import QCoreApplication, QSettings
from PyQt6.QtGui import QGuiApplication, QIcon
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtQuick import QQuickWindow

from preview import Preview


QQuickWindow.setSceneGraphBackend('software')

qApp = QGuiApplication(sys.argv)

QCoreApplication.setOrganizationName("Deuteronomy Works")
QCoreApplication.setApplicationName("Ninja-Preview")
settings = QSettings()

qApp.setWindowIcon(QIcon("UI/icons/logo.png"))

engine = QQmlApplicationEngine()

preview = Preview()

engine.load("UI/main.qml")
engine.rootObjects()[0].setProperty('preview', preview)
engine.quit.connect(qApp.quit)

sys.exit(qApp.exec())

# -*- coding: utf-8 -*-
import sys
import platform
from PyQt5.QtCore import QCoreApplication, QSettings, QResource
from PyQt5.QtGui import QGuiApplication, QIcon
from PyQt5.QtQml import QQmlApplicationEngine
from preview import WinPreview, UnixPreview
from install_func import install_font

qApp = QGuiApplication(sys.argv)

QCoreApplication.setOrganizationName("Deuteronomy Works")
QCoreApplication.setApplicationName("Ninja-Preview")
settings = QSettings()
QResource.registerResource("resources.rcc")

qApp.setWindowIcon(QIcon(":/UI/icons/logo.ico"))

# install functions
install_font()

engine = QQmlApplicationEngine()

os_name = platform.system()

if os_name == 'Windows':
    preview = WinPreview()
else:
    preview = UnixPreview()

engine.rootContext().setContextProperty('preview', preview)

engine.load('qrc:///UI/main.qml')

engine.quit.connect(qApp.quit)

sys.exit(qApp.exec_())

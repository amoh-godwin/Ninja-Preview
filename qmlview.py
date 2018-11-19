# -*- coding: utf-8 -*-
import sys
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine


def run():
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.load(sys.argv[1])
    sys.exit(app.exec_())

    return 0


if len(sys.argv) > 1:
    run()
else:
    print('Usage: qmlview file')

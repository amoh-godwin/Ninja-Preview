# -*- coding: utf-8 -*-
import sys
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from preview import Preview
class App():


    def __init__(self):


        super.__init__
        self.preview = ()
        self._preprocesses()


    def _postprocess(self):
        """
        """

    def _preprocesses(self):
        """
        
            Start the Manager class
        
        """
        self.preview = Preview()

        self._start()

    def _start(self):


        qApp = QGuiApplication(sys.argv)
        """qApp.setWindowIcon(QIcon("/assets/image/logo_GGuides.ico"))"""

        engine = QQmlApplicationEngine()
        engine.rootContext().setContextProperty('preview', self.preview)
        engine.load('UI/main.qml')
        engine.quit.connect(qApp.quit)

        qApp.aboutToQuit.connect(self._postprocess)
        qApp.exec_()

        sys.exit()


App()




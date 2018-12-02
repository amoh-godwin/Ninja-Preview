import os
import subprocess
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot

class Preview(QObject):
    """
    """

    def __init__(self):
        QObject.__init__(self)

    @pyqtSlot(str)
    def run(self, filename):
        pass

    def _run(self, filename):
        cwd = os.getcwd()
        os.chdir(os.path.join(cwd, "App/qmlview/qmlview"))
        out = subprocess.check_output(['qmlview',
                                       filename],
                                       shell=True)

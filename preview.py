import os
import subprocess
import threading
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot

class Preview(QObject):
    """
    """

    def __init__(self):
        QObject.__init__(self)

    logger = pyqtSignal(str, arguments=['_run'])

    @pyqtSlot(str)
    def run(self, filename):
        # Start a thread to handle process
        run_thread = threading.Thread(target = self._run, args=[filename])
        run_thread.start()

    def _run(self, filename):
        print('right here')
        out = subprocess.check_output(['qmlview',
                                       filename,],
                                       shell=True)
        print(out)

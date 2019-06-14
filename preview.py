import os
import subprocess
import threading
from time import sleep
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot


class Preview(QObject):
    """
    """

    def __init__(self):
        QObject.__init__(self)
        self.process_running = False
        self.app_closed = False
        self.output = b''

    logger = pyqtSignal(str, arguments=['_run'])

    @pyqtSlot(str)
    def run(self, filename):
        # Start a thread to handle process
        run_thread = threading.Thread(target=self._run, args=[filename])
        run_thread.start()
        monitor_thread = threading.Thread(target=self._monitor)
        monitor_thread.start()

    def _run(self, filename):
        print('right here')
        self.process_running = True
        if os.name == 'nt':
            self.output += subprocess.check_output(['qmlview',
                                                    filename, ],
                                                   stderr=subprocess.STDOUT,
                                                   shell=True)
        else:
            cmd = './qmlview ' + filename
            self.output = os.system(cmd)
        self.process_running = False
        print(self.output)

    def _monitor(self):
        # monitor a change in the output variable
        while (self.process_running and not self.app_closed):
            sleep(0.3)
            print(self.output)

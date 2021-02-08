import sys
import os
import subprocess
import threading
import platform
from time import sleep
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot


class Preview(QObject):
    """
    """

    def __init__(self):
        QObject.__init__(self)
        self.process_running = False
        self.app_closed = False
        self.err_chk_on = False
        self.break_check = False
        self.err_chk_called = False
        self.output = b''

        # hot reload
        self.hot_reload_indeces = []

        # user local qmlview
        if platform.system() == 'Windows':
            cwd = os.path.dirname(sys.argv[0])
            cwd = "H:\\GitHub\\Qmlview\\dist\\qmlview"
            self.qmlview = '"' + os.path.join(cwd, 'qmlview.exe') + '"'
        else:
            self.qmlview = './qmlview'

    log = pyqtSignal(str, arguments=['_monitor'])
    bootedUp = pyqtSignal(str, arguments=['bootValue'])
    hotReloadExit = pyqtSignal(int, arguments=[''])

    @pyqtSlot(str)
    def bootUp(self, status):
        if status == 'Loaded':
            self.find_qt_version()

    @pyqtSlot(str, int)
    def run(self, filename, view_index):
        # Start a thread to handle process
        run_thread = threading.Thread(target=self._run, args=[filename,
                                                              view_index])
        run_thread.daemon = True
        run_thread.start()
        return

    @pyqtSlot(str, int)
    def run_in_hot_reload_mode(self, filename, view_index, index=0):
        run_thread = threading.Thread(target=self._run_in_hot_reload_mode,
                                      args=[filename, view_index, index])
        run_thread.daemon = True
        run_thread.start()
        return

    @pyqtSlot(str, int)
    def run_in_phone_frame(self, filename, view_index):

        run_thread = threading.Thread(target=self._run_in_phone_frame,
                                      args=[filename, view_index])
        run_thread.daemon = True
        run_thread.start()
        return

    def _run(self, filename, view_index):
        self.process_running = True

        command = self.qmlview + ' ' + '"' + filename + '"'

        subP = subprocess.Popen(command,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT,
                                shell=True)
        monitor_thread = threading.Thread(target=self._monitor,
                                          args=[subP, view_index],
                                          daemon=True)
        monitor_thread.start()

    def _run_in_hot_reload_mode(self, filename, view_index, index=0):

        print(view_index, index)

        # Add to hot reload indeces
        if view_index not in self.hot_reload_indeces:
            self.hot_reload_indeces.append(index)

        # Now call to run
        command = self.qmlview + ' ' + '"' + filename + '"' + ' --live'

        subP = subprocess.Popen(command,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT,
                                shell=True)
        monitor_thread = threading.Thread(target=self._monitor,
                                          args=[subP, view_index],
                                          daemon=True)
        monitor_thread.start()

    def _run_in_phone_frame(self, filename, view_index):

        command = self.qmlview + ' ' + '"' + filename + '"' + ' --phone'

        subP = subprocess.Popen(command,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT,
                                shell=True)
        monitor_thread = threading.Thread(target=self._monitor,
                                          args=[subP, view_index],
                                          daemon=True)
        monitor_thread.start()

    def find_qt_version(self):
        find_thread = threading.Thread(target=self._find_qt_version,
                                       args=[],
                                       daemon=True)
        find_thread.start()

    def _find_qt_version(self):
        qt_version = ''
        
        command = self.qmlview + ' ' + '-v'
        
        subP = subprocess.Popen(command,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT,
                                shell=True)

        ret = subP.stdout.read()
        subP.kill()

        qt_version = str(ret[:-2], 'utf-8')
        if '5' in qt_version:
            pass
        else:
            qt_version = ''
        self.bootValue(qt_version)

    def bootValue(self, value):
        self.bootedUp.emit(value)

    def _monitor(self, obj, view_index):
        # monitor a change in the output variable
        while (self.process_running and not self.app_closed):
            # just added
            # read one char from stdout
            char = obj.stdout.read(1)
            # check if error checking is on
            if char == '':
                length = 0
            # length = obj.stdout.tell()
            if self.err_chk_on and length == 0:
                if length == 0:
                    # wait seven seconds since it takes at least
                    # five for the error checking to be done
                    # and repeat the loop to verify what happened
                    sleep(3)
                    continue

            # read one char from stdout
            # char = obj.stdout.read(1)  ***

            # if the one char is a newline
            # this is normal, it supposed to be at the end
            # of each response
            if char == b'\n':
                # add the char to the output
                self.output += char

                # if after adding the character we still
                # have just a newline
                # then, there were two newlines
                # since we break on newlines, this should happen
                # unless there were two
                # the second argument self.err_chk_on ensures;
                # we do not run this code twice to check for the
                # same error since this loop will continue whiles
                # error_checking is going on
                if self.output == b'\n' and not self.err_chk_on:

                    # clean slate for err_checking
                    self.output = b''

                    # set that error_checking is going on
                    self.err_chk_on = True
                    err_chk_thread = threading.Thread(
                                            target=self._error_checking,
                                            args=[obj])
                    err_chk_thread.daemon = True
                    err_chk_thread.start()
                    # continue

                # if someother character is detected whiles
                # error checking is on then stop the error check
                # it isn't an error
                elif self.output != b'\n' and self.err_chk_on:
                    self.break_check = True

                # Send output to UI layer
                self.log.emit(str(view_index) + ":::" + str(self.output,
                                                            'utf-8'))

                # Get a clean slate and
                # wait 0.3 seconds then repeat
                self.output = b''
                sleep(0.3)

            # If for some wierd reason the process is running
            # and there is nothing in it
            elif char == b'':
                # check if the process hasn't finished
                # then end it yourself
                if obj.returncode is None:
                    break
                else:
                    # do nothing
                    pass
            # it is just a normal character add and lets continue
            # this is one of the two required
            else:
                self.output += char

        # we are out of loop
        # calculate exit code
        if self.err_chk_called:
            exit_code = '1x0000'
        else:
            exit_code = '0'

        # reset the variable
        self.err_chk_called = False

        # emit the exit codes
        self.log.emit(str(view_index) + ":::" + "process has exited")
        self.log.emit(str(view_index) + ":::" + 'exit code: ' + exit_code)
        if view_index in self.hot_reload_indeces:
            self.hotReloadExit.emit(view_index)
            self.hot_reload_indeces.remove(view_index)
        return

    def _error_checking(self, obj):

        # wait before start
        self.err_chk_called = True
        count = 0
        while (self.process_running and not self.app_closed and not
               self.break_check):

            if count > 2:
                # kill the POpen process
                obj.kill()
                # try to delete it
                # obj = None
                # stop the process
                self.process_running = False
                break

            # if output has not added any data to it
            # then it's probable the error we are looking for
            elif self.output == b'':
                count += 1
                sleep(1)

            else:
                # not an error
                break

        # Reset the variables
        self.err_chk_on = False
        self.break_check = False

    def end_read(self):
        sleep(0.3)
        # change directory back to avoid any crashes
        # os.chdir(default_path)
        self.process_running = False

from PyQt5.QtCore import QThread, QWaitCondition, QMutex, pyqtSignal
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QProgressBar


class Thread(QThread):

    valueChange = pyqtSignal(int)

    def __init__(self, *args, **kwargs):
        super(Thread, self).__init__(*args, **kwargs)
        self._isPause = False
        self._value = 0
        self.cond = QWaitCondition() #
        self.mutex = QMutex()        #

    def pause(self):
        self._isPause = True

    def resume(self):
        self._isPause = False
        self.cond.wakeAll()

    def run(self):
        while 1:
            self.mutex.lock() # thread 하나만 들어가게 한다.
            if self._isPause:
                self.cond.wait(self.mutex) # mutex를 넣는다.

            if self._value > 100:
                self._value = 0

            self._value += 1
            self.valueChange.emit(self._value)
            self.msleep(100)
            self.mutex.unlock() # thread 하나만 들어가게 한다.

class Window(QWidget):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        layout = QVBoxLayout(self)
        self.progressBar = QProgressBar(self)
        layout.addWidget(self.progressBar)
        layout.addWidget(QPushButton('정지', self, clicked=self.doWait))   # clicked에 self.doWait 함수가 동작
        layout.addWidget(QPushButton('깨어남', self, clicked=self.doWake)) # clicked에 self.doWake 함수가 동작

        self.t = Thread(self)
        self.t.valueChange.connect(self.progressBar.setValue)
        self.t.start() # run이 실행된다.

    def doWait(self):
        self.t.pause()

    def doWake(self):
        self.t.resume()


if __name__ == '__main__':
    import sys
    import cgitb
    sys.excepthook = cgitb.enable(1, None, 5, '')
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())

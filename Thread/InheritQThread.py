from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QProgressBar, QPushButton


# thread에 대한 class를 정의 -> run이라는 method를 가지고 있어야 한다.
class Thread(QThread):

    valueChanged = pyqtSignal(int) # 클래스 멤버변수

    def run(self):
        print('Thread id', int(QThread.currentThreadId()))
        for i in range(1, 101):
            print('value', i)
            self.valueChanged.emit(i) # 방사, 방출
            QThread.sleep(1)


class Window(QWidget): # 메인 view

    def __init__(self, *args, **kwargs ):
        super(Window, self).__init__(*args, **kwargs)
        layout = QVBoxLayout(self)            # layout 만들고
        self.progressBar = QProgressBar(self) # ProgressBar에 대한 객체 만들고
        self.progressBar.setRange(0, 100)
        layout.addWidget(self.progressBar)
        layout.addWidget(QPushButton('이것은_버튼', self, clicked=self.onStart))
        
        print('main id', int(QThread.currentThreadId()))

        self._thread = Thread(self)
        # 이친구는 원래 등록된 signal인가 보다.
        self._thread.finished.connect(self._thread.deleteLater)
        # 이친구는 우리가
        self._thread.valueChanged.connect(self.progressBar.setValue)

    def onStart(self): # thread의 함수중 start()를 정의하는 함수
        print('main id', int(QThread.currentThreadId()))
        self._thread.start()

    def closeEvent(self, event): # thread의 함수중 quit()를 정의하는 함수
        if self._thread.isRunning():
            self._thread.quit()
        del self._thread # thread를 삭제
        super(Window, self).closeEvent(event)

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())


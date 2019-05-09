import sys

from PyQt5.QtCore import Qt
from QWidget.CustomPaintWidget import CustomPaintWidget
from QWidget.CustomWidget import CustomWidget
# QtWidgets 를 사용하기 위함!
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout

class Window(QWidget):
## ** self를 인자에 넣는 다는 것은 Window 안에 넣는 다는 것이다. **

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        layout = QHBoxLayout(self)
        # Horizontal로 쌓인다.
        layout.addWidget(CustomPaintWidget(self))
        layout.addWidget(CustomWidget(self))
        # layout에 Widget을 추가
        w = CustomWidget(self)
        w.setAttribute(Qt.WA_StyledBackground) # Indicates the widget should be drawn using a styled background.
        layout.addWidget(w)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # CustomPaintWidget과 CustomWidget에
    # 대한 style을 지정한다.
    app.setStyleSheet('''
    CustomPaintWidget { min-width: 120px;
                        min-height: 80px;
                        border: 1px solid green; 
                        border-radius: 20px; 
                        background: red; 
                        } 
                        
    CustomWidget { min-width: 200px;
                   min-height: 200px;
                   max-width: 200px;
                   max-height: 200px;
                   border: 1px solid orange;
                   border-radius: 100px;
                   background: blue;
                   }
    '''
    )
    w = Window()
    w.show()
    sys.exit(app.exec_())

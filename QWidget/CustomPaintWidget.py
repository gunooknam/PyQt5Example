from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QStyleOption, QStyle


class CustomPaintWidget(QWidget):

    def __init__(self, *args, **kwargs):
        super(CustomPaintWidget, self).__init__(*args, **kwargs)
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("[ I'm PaintWidget!! ]",self))

    def paintEvent(self, event):
        option = QStyleOption()
        option.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget,
                                   option,
                                   painter,
                                   self)

        super(CustomPaintWidget, self).paintEngine()

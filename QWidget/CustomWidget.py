from PyQt5.QtWidgets import  QWidget, QVBoxLayout, QLabel

class CustomWidget(QWidget):

    def __init__(self, *args, **kwargs):
        super(CustomWidget, self).__init__(*args, **kwargs)
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("[ I'm Custom Widget!! ]", self))

from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MyHWidget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("Horizontal Layout")
        self.resize(350,100)
        main_layout = QHBoxLayout(self)
        btn_1 = QPushButton("按钮1",self)
        btn_2 = QPushButton("按钮2",self)
        btn_3 = QPushButton("按钮3",self)
        main_layout.addWidget(btn_1)
        main_layout.addWidget(btn_2)
        main_layout.addWidget(btn_3)

        btn_1.installEventFilter(self)
        self.installEventFilter(self)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_A :
            print("Key A Press")
    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_A :
            print("Key A Release")

    def eventFilter(self, obj, e):
        print(obj)
        print(e)
        print(e.type())

        return QObject.eventFilter(self, obj, e) 



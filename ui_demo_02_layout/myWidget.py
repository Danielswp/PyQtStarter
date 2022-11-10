from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 


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
        #self.setLayout(main_layout)

class MyVWidget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("Vertical Layout")
        self.resize(350,100)
        main_layout = QVBoxLayout(self)
        btn_1 = QPushButton("按钮1",self)
        btn_2 = QPushButton("按钮2",self)
        btn_3 = QPushButton("按钮3",self)
        main_layout.addWidget(btn_1)
        main_layout.addWidget(btn_2)
        main_layout.addWidget(btn_3)
        #self.setLayout(main_layout)

class MyGWidget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("Grid Layout")
        self.resize(350,100)
        main_layout = QGridLayout(self)
        btn_1 = QPushButton("按钮00",self)
        btn_2 = QPushButton("按钮01",self)
        btn_3 = QPushButton("按钮10",self)
        btn_4 = QPushButton("按钮11",self)
        main_layout.addWidget(btn_1,0,0)
        main_layout.addWidget(btn_2,0,1)
        main_layout.addWidget(btn_3,1,0)
        main_layout.addWidget(btn_4,1,1)
        #self.setLayout(main_layout)

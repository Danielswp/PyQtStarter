# Class QObject  pyqtSignal()
# PyQt5.QtCore.pyqtSignal
# [int], [str], [list], [tuple], [dict], [bool]


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import pyqtSignal


class MyHWidget(QWidget):
    # python基本数据类型-----int, str, list, tuple, dict, bool 
    callMe = pyqtSignal([str])
    canCallMe = pyqtSignal(str,bool)

    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("Horizontal Layout")
        self.resize(350,100)
        main_layout = QHBoxLayout(self)
        btn_1 = QPushButton("按钮1",self)
        self.__btn_2 = QPushButton("按钮2",self)
        btn_3 = QPushButton("按钮3",self)
        main_layout.addWidget(btn_1)
        main_layout.addWidget(self.__btn_2)
        main_layout.addWidget(btn_3)

        #对象.信号.connect(方法)
        btn_1.clicked.connect(lambda : print("btn_1 clicked"))

        fun1 = lambda : print("btn2 clicked")
        #对象.信号.connect(方法)
        print(fun1)
        self.__btn_2.clicked.connect(fun1)
        btn_3.clicked.connect(self.onBtn3Clicked)

    def onBtn3Clicked(self):
        print("handle Btn3 clicked.")
        self.callMe.emit("测试")
        self.canCallMe.emit("小明",True)



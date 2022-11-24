from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import platform


class MyHWidget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("QGet")
        self.resize(800,600)
        main_layout = QHBoxLayout(self)
        btn_1 = QPushButton("按钮1",self)
        btn_2 = QPushButton("按钮2",self)
        btn_3 = QPushButton("按钮3",self)
        main_layout.addWidget(btn_1)
        main_layout.addWidget(btn_2)
        main_layout.addWidget(btn_3)

        #btn_1.installEventFilter(self)
        #self.installEventFilter(self)

    def showinfo(self, tip, info):
        print("{}:{}".format(tip,info))
 


    def keyPressEvent(self, event):
        if event.key() == Qt.Key_A :
            print("Key A Press")

            self.showinfo("操作系统及版本信息",platform.platform())
            self.showinfo('获取系统版本号',platform.version())
            self.showinfo('获取系统名称', platform.system())
            self.showinfo('系统位数', platform.architecture())
            self.showinfo('计算机类型', platform.machine())
            self.showinfo('计算机名称', platform.node())
            self.showinfo('处理器类型', platform.processor())
            self.showinfo('计算机相关信息', platform.uname())
    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_A :
            print("Key A Release")

    def eventFilter(self, obj, e):
        return QObject.eventFilter(self, obj, e) 



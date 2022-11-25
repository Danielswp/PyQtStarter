from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from pyquery import PyQuery as pq
import requests



class MyHWidget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("QGet")
        self.resize(800,600)
        main_layout = QHBoxLayout(self)
        self.btn_1 = QPushButton("按钮1",self)
        btn_2 = QPushButton("按钮2",self)
        btn_3 = QPushButton("按钮3",self)
        main_layout.addWidget(self.btn_1)
        main_layout.addWidget(btn_2)
        main_layout.addWidget(btn_3)

        self.btn_1.clicked.connect(self.getHttpProxyInfo)

    def getHttpProxyInfo(self):
        # url = 'https://www.kuaidaili.com/free/'
        # headers = {
        #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'
        # }
        # r = requests.get(url,headers=headers)
        # #self.debugRequestsGet(r)
        # proxyInfo = pq(r.text)
        # for item in proxyInfo('tbody tr').items():
        #     for col in item('td').items():
        #         col_key = col.attr('data-title')
        #         col_value = col.text()

 



    def debugRequestsGet(self, r):
        print(type(r))
        print(r.status_code)
        print(type(r.text))
        print(r.text)
        print(r.cookies)
 






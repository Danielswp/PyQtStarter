import sys
from PyQt5.QtCore import *
from myWidget import *


if __name__ == "__main__":
	app = QApplication(sys.argv)
	win1 = MyHWidget()
	win1.show()

	# fun1 = lambda : print("btn2 clicked")
	# #对象.信号.connect(方法)
	# print(fun1)
	# win1.__btn_2.clicked.connect(fun1)

	fun2 = lambda a : print("处理:"+ a)
	win1.callMe.connect(fun2)
	
	win1.callMe.disconnect(fun2)

	fun3 = lambda a, b : print("处理2:"+ a + " ==>"+str(b))
	win1.canCallMe.connect(fun3)

	sys.exit(app.exec_())

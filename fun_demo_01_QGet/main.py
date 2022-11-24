import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from myWidget import *


if __name__ == "__main__":
	app = QApplication(sys.argv)
	# win1 = MyHWidget()
	# win1.show()

	val = 3.1415926e-5
	print(val)
	str = QString.number(val,'f',2)
	print(val)

	sys.exit(app.exec_())

import sys
from PyQt5.QtCore import *
from myWidget import *


if __name__ == "__main__":
	app = QApplication(sys.argv)
	win1 = MyHWidget()
	win1.move(QPoint(10,100))
	win1.show()

	# win2 = MyVWidget()
	# win2.show()

	# win3 = MyGWidget()
	# win3.show()

	sys.exit(app.exec_())

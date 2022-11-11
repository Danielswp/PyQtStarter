import sys
from PyQt5.QtCore import *
from myWidget import *


if __name__ == "__main__":
	app = QApplication(sys.argv)
	win1 = MyHWidget()
	win1.show()

	sys.exit(app.exec_())

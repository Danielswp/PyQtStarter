import sys
from PyQt5.QtWidgets import *
from firstMainWin import *

class MyMainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self,parent=None):
		super(MyMainWindow,self).__init__(parent)
		self.setupUi(self)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	win = MyMainWindow()
	#print(win)
	win.show()
	sys.exit(app.exec_())

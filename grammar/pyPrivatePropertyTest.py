class TestClass:
	__id = "jack897"
	count = 1

	def __init__(self):
		pass

	def showId(self):
		print("id:"+ self.__id);

	def __myFun(self):
		print("    内部方法")

	def show(self):
		print("外部方法")

	def showMyFun(self):
		print("showMyFun=====>")
		self.__myFun()





if __name__ == "__main__":
	obj = TestClass()
	obj.show()

	# !error
	# obj.__myFun()

	obj.showMyFun()

	print(obj.count)
	obj.count = 789
	print(obj.count)

	# !error
	# print(obj.__id)

	obj.showId()
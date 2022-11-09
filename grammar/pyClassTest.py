class MyClass:
	count = 0
	name = 'DefaultName'

	def __init__(self, name):
		self.name = name
		str = '类的变量是%s\n对象的变量是%s'%(MyClass.name, self.name)
		print(str)\

	def setCount(self, count):
		self.count = count

	def getCount(self):
		return self.count


if __name__ == "__main__":
	cls = MyClass('lisi')
	cls.setCount(10)
	str = 'count=%d'%cls.getCount()
	print(str)
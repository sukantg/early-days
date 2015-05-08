class classA:

	def __init__(self,data):
		self.data = data

	def display(self):
		print (self.data)

class classB(classA):

	def display(self):
		print ('Coming from B = %s' % self.data)

class classC(classB):
	def __add__(self,toAdd):
		return classC(self.data + toAdd)

	def mult(self,toMul):
		self.data *= toMul

	def __str__(self):
		return 'classC = %s' % self.data


c = classC("123")
print c


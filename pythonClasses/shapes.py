class Rectangle:

	def __init__(self,wid,hei):
		self.width = wid
		self.height = hei

	def getWidth(self):
		return self.width

	def setWidth(self,w):
		self.width = w

	def getHeight(self):
		return self.height

	def setHeight(self,h):
		self.height = h

	def getArea(self):
		return self.getWidth() * self.getHeight()

	def __repr__(self):
		return 'Rectangle - %s' %(self.getArea())


class Square:

	def __init__(self,side):
		self.length = side

	def getLength(self):
		return self.length

	def setLength(self,s):
		self.length = s

	def getSquare(self):
		return self.length ** 2

	def __str__(self):
		return 'Length - %s, Squared Value - %s' % (self.getLength(),self.getSquare())

	V = property(getSquare)



s = Square(10)
print s
print s.V

r = Rectangle(12,12)
print r

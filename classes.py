# A simple program to understand classess
"""
# Defining a class..
class class_name:
	[statement 1]
	[statement 2]
	[statement 3]
	[etc]

"""

class shape:
	"""No description yet"""
	def __init__(self, x, y):
		(shape, self).__init__()
		self.x = x
		self.y = y
	description = "This is a shape class."
	author = "Kartik Jagdale"
	def area(self):
		return self.x * self.y
	def perimeter(self):
		return 2 * self.x + 2 * self.y
	def describe(self, text):
		self.description = text
	def authorName(self, text):
		self.author = text
	def scaleSize(self, scale):
		self.x = self.x*scale
		self.y = self.y*scale


rec = shape(100,20)
print 'Area is :',rec.area()
print 'Perimeter is :',rec.perimeter()
rec.describe("Hi this is a description")
rec.authorName("Kartik")
print rec.description
print rec.author
rec.scaleSize(0.5)
print 'After scaling' rec.x, rec.y
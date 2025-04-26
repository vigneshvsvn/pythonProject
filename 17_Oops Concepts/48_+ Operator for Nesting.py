class Book:
	def __init__(self,pages):
		self.pages=pages

	def __add__(self, other):       ## magic Methods available for each operator
		totalPages=self.pages+other.pages
		return Book(totalPages)
		##return  totalPages

	def __str__(self):
		return f"{self.pages}"


b1=Book(10)
b2=Book(20)
b3=Book(20)
print(b1+b2)
print(b1+b2+b3)  ## not possible      TypeError: unsupported operand type(s) for +: 'int' and 'Book'
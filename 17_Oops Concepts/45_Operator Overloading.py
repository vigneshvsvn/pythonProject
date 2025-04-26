"""
Applying or using  Same Operator  for Multiple purpose.

+ Operator:
a=10+20     '+' Operator will perform arithmetic Operation if operand type is INT
b='10'+'20' '+' Operator will perform concatenation, if operand are string

* Operator:
a=10*20   --> multiplication
b='Vignesh' * 10 --> Became repetition Operator.

We can use of Objects as well in Python.

"""

class Book:
	def __init__(self,pages):
		self.pages=pages

	def __add__(self, other):       ## magic Methods available for each operator
		totalPages=self.pages+other.pages
		return  totalPages


b1=Book(10)
b2=Book(20)
b3=Book(20)
print(b1+b2)
print(b1+b2+b3)  ## not possible      TypeError: unsupported operand type(s) for +: 'int' and 'Book'




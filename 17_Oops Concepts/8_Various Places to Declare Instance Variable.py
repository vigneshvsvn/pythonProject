"""
We can Declare in 3 places.
1. Inside constructor using self
2. Inside instance Method using self
3. Outside the class using by using Object reference Variable.

"""



class Test:
	def __init__(self):  # inside constructor using self
		self.a=10
		self.b=20

	def m1(self): # Inside Instance Method using self
		self.c=30

t=Test()
t.m1()
t.d=40  ## outside of Class using Class reference variabl
print(t.__dict__)


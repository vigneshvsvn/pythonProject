"""
To access  parent class Instance variable we can't use with super() from child class .
We have to use self only.

If both parent and child class have same instance variable. Then it's not possible to access parent instance using self als.
It will give only child class self

"""

class Parent:
	a=888
	def __init__(self):
		self.b=999

class Child(Parent):
	
	def m1(self):
		print(self.a)
		print(self.b)
		print(super().a)
		##print(super().b)     ### it will through an Error.

c=Child()
c.m1()
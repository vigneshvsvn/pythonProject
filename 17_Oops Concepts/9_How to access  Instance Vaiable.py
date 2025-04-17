"""
Access of instance variable:
	1. Inside Class we can access using self(instance/object reference)   only inside constructor and instance Method.
	2. outside class using object reference we can access.

Deletion of Instance Variable:

1. inside class.
	del self.c
2. outside of class
	del t.a

"""



class Test:
	def __init__(self):
		self.a=10
		self.b=20

	def display(self):
		print(self.a)
		print(self.b)
		del self.a

t=Test()
t.display()

print(t.a)  ## as it's deleted when we call t.display()     AttributeError: 'Test' object has no attribute 'a'

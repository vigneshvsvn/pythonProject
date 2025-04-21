"""
Static Methods: Don't use instance Variable and static Variable. Such type of methods called static Method.
	- Utility Method.
	-@staticmethod decorator need use
	- we can call static method using object reference or Class Name. Recommended to use by class name.
"""

class Test:
	@staticmethod
	def add(a,b):
		print("The Sum :",a+b)
	@staticmethod
	def product(a,b):
		print("Product:",a*b)
	@staticmethod
	def average(a,b):
		print("Average:",(a+b)/2)

Test.add(50,40)
Test.product(40,40)
Test.average(40,50)


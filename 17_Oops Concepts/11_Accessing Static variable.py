"""
1. Inside Constructor: By using Class name(is recommended ) or self
2. Inside Instance Method: By using Class name(is recommended ) or self
3. Inside Class Method: By using Class name or class reference variable
4. Inside Static Method : By using Class Name
5. OUtside of the class either by object reference or class Name
"""

class Test:
	a=10
	def __init__(self):
		print("Inside Constructor print Using Self ",self.a)
		print("Inside Constructor Print using Class name",Test.a)

	def m1(self):
		print("Inside Instance Method using self",self.a)
		print("Inside Instance Method using class Name",Test.a)

	@classmethod
	def clsMethod(cls):
		print("Inside Class Method using cls reference:",cls.a)
		print("Inside Class Method using class name: ",Test.a)

	@staticmethod
	def m3( ):
		print("Inside Static Method:",Test.a)

t1=Test()
t1.m1()
t1.clsMethod()
t1.m3()
print("Out side of Class",Test.a)


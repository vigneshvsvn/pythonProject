"""
- We can Modify static variable anywhere  by class name inside/outside of class name
- cls class reference variable or class name inside class method

"""


class Test:
	a=10
	def __init__(self):
		Test.a=20     ## modified in sid constructor
		self.a=100    ## If we use self it will create instance variable not class variable
		print("Inside Constructor print Using Self ",self.a)
		print("Inside Constructor Print using Class name",Test.a)

	def m1(self):
		Test.a=30
		self.a=300    ## If we use self it will create instance variable not class variable
		print("Inside Instance Method using self",self.a)
		print("Inside Instance Method using class Name",Test.a)

	@classmethod
	def clsMethod(cls):
		cls.a=40
		print("Inside Class Method using cls reference:",cls.a)
		print("Inside Class Method using class name: ",Test.a)

	@staticmethod
	def m3( ):
		Test.a=50
		print("Inside Static Method:",Test.a)

print("Initial value:",Test.a)
t1=Test()
t1.m1()
t1.clsMethod()
t1.m3()
Test.a=60
print("Out side of Class:",Test.a)



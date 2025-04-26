"""
super() is python inbuilt function used to access parent class Members ( methods,variable, consuructor) explicitly.

"""



class Parent:
	a=10
	def __init__(self):
		print("Parent Constructor")
	def m1(self):
		print("Parent Method.")
	@classmethod
	def m2(cls):
		print("Parent Class Method.")

	@staticmethod
	def m3():
		print("Parent Static Method.")


class Child(Parent):

	def __init__(self):
		print("Child Constructor.")

	def m1(self):
		print(super().a)
		super().m1()       ## call parent class m1() as we are using super(function)
		super().m2()
		super().m3()
		super().__init__()
		print("Child Method.")


c=Child()
c.m1()
"""
Inheritance or Is A relationship.
	- Parent to Child relationship
	- code reusability
	- Code Extendability    : Extending parent functionality + child existing functionality

"""

class Parent:
	def __init__(self):
		print("Parent Constructor..")
	def m1(self):
		print("Parent Method..")

class Child(Parent):  ## Means Child class inherited from  Parent class
	def __init__(self):     ## in case if child does not have constructor then  parent constructor will execute when we create child Object.
		print("Child Constructor...")
	def m2(self):
		print("Child Method...")
		self.m1()                    ## from Parent Class as we inherited the Parent class. So m2() is available for Child class

c=Child()
c.m2()

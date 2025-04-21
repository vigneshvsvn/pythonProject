"""
Class Defined inside another class.
	- Without existing one type object , if there is no chance of existing another type of Object
	- Inner Class object  always associated with Outer Class Object.

Advantage:
	- Improves Modularity
	- Improves security of application. With out outer class we can not use inner class functionality.
	
"""

class University: # outer Class. without University Object Department object is not possible
	class Department: ## inner class,
		pass

class Car:
	class Engine:
		pass

class Outer:
	def __init__(self):
		print("Outer Class Objected Created.")

	class Inner:
		def __init__(self):
			print("Inner Class Object Created.")

		def m1(self):
			print("Inner Class Method.")

obj1_outer=Outer()
obj1_inner=obj1_outer.Inner()
obj1_inner.m1()
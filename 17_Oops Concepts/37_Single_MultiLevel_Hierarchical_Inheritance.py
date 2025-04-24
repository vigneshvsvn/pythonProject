""""
1. Single Inheritance:  Inherit members of single Parent Class to Single Child Class.
Eg: Parent --> Child

 class Parent:
	def m1(self):
		print("Parent Class.")

class Child(Parent):
	def m2(self):
		print("Child class")

c=Child()
c.m1()
c.m2()

2. Multi level Inheritance:  Inherit Members of Multiple class with concept of one after other.
Eg: Parent --> Child --> GrandChild

class Parent:
	def m1(self):
		print("Parent Class.")

class Child(Parent):
	def m2(self):
		print("Child class")

class GrandChild(Child):
	def m3(self):
		print("Grand Children Class.")

c=GrandChild()
c.m1()
c.m2()
c.m3()

3. Hierarchical Inheritance: One Patent class with multiple child class. All child class are at same level.
Eg: Paranet --> Child 1 and Child 2

class Parent:
	def m1(self):
		print("Parent Class.")

class Child1(Parent):
	def m2(self):
		print("Child2 class")

class Child2(Parent):
	def m3(self):
		print("Child2class")

c1=Child1()
c2=Child2()

c1.m1()
c1.m2()

c2.m1()
c2.m3()

"""


class Parent:
	def m1(self):
		print("Parent Class.")

class Child1(Parent):
	def m2(self):
		print("Child2 class")

class Child2(Parent):
	def m3(self):
		print("Child2class")

c1=Child1()
c2=Child2()

c1.m1()
c1.m2()

c2.m1()
c2.m3()
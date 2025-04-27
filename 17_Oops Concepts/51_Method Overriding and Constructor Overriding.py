"""
Overriding : What ever  member present in parent class may not sufficient for  child  class.
So in child class we can redefine those members this is called overriding.
"""

class Parent:
	def __init__(self):
		print("Parent Constructor")
	def property(self):
		print("Land,Gold...")
	def marry(self):
		print("Kundhani")

class Child(Parent):
	def marry(self): ## This process of redefining parent class method in child class method  called Overriding.
		print("Samantha")

	def __init__(self):
		super().__init__()
		print("Child Constructor")

c=Child()
c.property()
c.marry()

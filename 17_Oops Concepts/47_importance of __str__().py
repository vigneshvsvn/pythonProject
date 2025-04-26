"""
__str__ -->     To get meaning full output. Then we need to override __str__ method explicitly.

"""

class Student:
	def __init__(self,name,rollnum,marks):
		self.name=name
		self.rollnum=rollnum
		self.marks=marks

	def __str__(self):
		return f"  name:{self.name},rollnum:{self.rollnum},marks:{self.marks}"


s1=Student('Vignesh',70,100)
s2=Student('Giri',71,90)
print(s1)
print(s2)
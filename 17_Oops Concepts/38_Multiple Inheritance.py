""""
Multiple: Inherit members of multiple parents to single Child class
		  Eg: Mom, Dad , Kid
class Dad:
	def m1(self):
		print("Dad knowledge.")

class Mom:
	def m2(self):
		print("Mother Logic")

class Kid(Dad,Mom):
	def m3(self):
		print("Kid Class.")

c=Kid()
c.m1()
c.m2()
c.m3()
"""

class Dad:
	def m1(self):
		print("Dad knowledge.")

class Mom:
	def m2(self):
		print("Mother Logic")

class Kid(Dad,Mom): ## Multiple parents with comma separations. Order is Important priority  will give to first parent
	def m3(self):
		print("Kid Class.")

c=Kid()
c.m1()
c.m2()
c.m3()
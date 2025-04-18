"""
Using only Class name or class reference (inside class method)
"""

class Test:
	a=10
	@classmethod
	def m1(cls):
		##del Test.a
		del cls.a



t1=Test()
print(Test.__dict__)
#t1.m1()
del Test.a
print(Test.__dict__)

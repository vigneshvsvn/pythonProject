"""
Group of statements repeatedly required then we need to go with Function.
	- If not using function length of code increase, Readability   reduce.

code which required repeatedly that has to write as Function. We need to call function whenever required unlimitedly .
- Biggest advantage is code reusability   so no duplicate code
Types of Functions:
1. Builtin Function or Predefined function
	- provided by python.
	- Eg: type(),print(),input(),int()......
2. User Defined or customized Function
	- WIll be done by programmer
	Syntax:
	def function_name(any number of Parameter):
		doc string using triple quote
		body  where actual code
		return value    (return is optional so  default return value is None)

"""


def calculate(a,b):
	print("sum :", a+b)
	print("Difference:",a-b)
	print("product:",a*b)

calculate(5,10)

calculate(9,6)
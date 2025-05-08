"""
Function having multiple decorators called decorator chaining.

EG: Bride input --> Facial Decor --> Hair Decor --> Dress Decor --> Bride output

"""

def decor1(func):
	def inner1():
		print("Decor 1 Execution.")
	return  inner1

def decor2(func):
	def inner2():
		print("Decor 2 Execution.")
	return inner2


@decor2
@decor1
def f():
	print("Original Function.")

f()
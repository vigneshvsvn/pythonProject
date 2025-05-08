def decor1(func):
	def inner1():
		print("Decor 1 Execution.")
		func()
	return  inner1

def decor2(func):
	def inner2():
		print("Decor 2 Execution.")
		func()
	return inner2


@decor2
@decor1
def f():
	print("Original Function.")

f()
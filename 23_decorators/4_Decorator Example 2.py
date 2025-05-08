
def decor_for_add(input_function):
	def inner(a,b):
		print("#"*30)
		print("The Sum:",end='')
		input_function(a,b)
		print("#" * 30)

	return inner

@decor_for_add
def add(a,b):
	print(a+b)

add(10,20)
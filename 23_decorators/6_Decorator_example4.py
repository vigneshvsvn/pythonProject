def smart_division(input_function):
	def inner(a,b):
		if b==0:
			print("Hello, how can you divide by Zero. Correct your value of b")
		else:
			input_function(a,b)
	return inner

@smart_division
def division(a,b):
	print(a/b)

division(10,2)
division(10,0)
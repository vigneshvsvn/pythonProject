def decor(input_function):
	def inner(name):
		if name=='Samantha':
			print('#'*30)
			print("Hello Samantha, You are very Important for us...")
			print("Very Very Good Morning.")
			print('#' * 30)
		else:
			input_function(name)
	return inner



@decor
def wish(name):
	print("Good Morning!",name)

wish('Sam')
wish("Samantha")
def decor(input_function):
	def inner(name):
		if name=='Samantha':
			print('#'*30)
			print("Hello Samantha, You are very Important for us...")
			print("Very Very Good Morning. We need your call sheet")
			print('#' * 30)
		else:
			input_function(name)
	return inner


def wish(name):
	print("Good Morning!",name)

decorated_wish=decor(wish)  ## this will have reference of inner() with in decor()

print("Before Hit Movies.")
wish('Samantha')
print("After Hit Movies..")
decorated_wish('Samantha')
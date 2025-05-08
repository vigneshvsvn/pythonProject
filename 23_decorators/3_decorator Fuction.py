"""
decorator Fuction: Used for Decoration function.

input function --> Decorator function --> output function.

Decorator function:
- takes input argument as function
-  return function as output

"""
## Basic syntax of Decorator Method
def decorator_function(input_function):
	def output_function():
		print("Add Extra power/work")
	return output_function

##Example1:

def decor(input_fun):
	def inner():
		print("Send the person to Beauty Parlour.")
		print("Showing a person with full of Make up.")
	return  inner	

@decor ## associated with decor function
def display():
	print("Showing a person as it is.")

display()
"""
Once we call display() it find @decor. 
	so display() will not execute, instead decor() will be called by passing display as input Function.
	and returned inner() will be executed.
	
	Note: number of argument of display() and inner() should be same. 
"""
	
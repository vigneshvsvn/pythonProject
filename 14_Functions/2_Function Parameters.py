"""
- parameters of function act as inputs to the Function
	If we are giving parameter in function then while calling it's mandatory to pass arguments.
"""

def wish(name):
	print(f"Hello {name}! Welcome to Learn Python Function")

def square_number(num):
	print(f"Square Value of number {num}: ",num**2)

def square_num(num) :
	return num ** 2
def fact(num):
	result=1
	while num >=1:
		result=result*num
		num=num-1
	return result
		

wish('Vignesh')
wish('Priya')
wish('Privika')
square_number(10)

print(f"Square Value of number {200}:",square_num(200))

print("factorical of Give Number 5:", fact(5))
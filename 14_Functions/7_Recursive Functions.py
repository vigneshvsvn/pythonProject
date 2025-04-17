"""
Function that call's itself called Recursive Functions.

Advantages:
	1. Solve complex problems very easily
	2. Length of the code will be reduced and readability will be increased.

Limitation:
Only 997 times we can call   RecursionError: maximum recursion depth exceeded in comparison
 factorial(998)  --> will give error 
"""

def factorial(n):
	if n==0:
		result=1
	else:
		result=n*factorial(n-1)   ##factorial function call itself in the same function. This is called Recursion.

	return result

print("The Factorial of 5 is ",factorial(998))
"""
Tracing of above 
n=5


"""
		
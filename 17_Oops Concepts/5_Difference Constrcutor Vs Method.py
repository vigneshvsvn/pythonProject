"""
Methods:
	  - Any name we can use for Method.
	  - Any number of time we can call Method.
	  - We have to call explicitly then only it will execute.
	  - Inside Method we need to write Business Logic

Constructor:
	- Constructor name is fixed (__init__(self))
	- Only one when we create Object.
	- When ever we create object, Constructor will execute automatically. We are not required to call explicitly. If we want we can call explicitly as well.
	- Declaration of Instance variables and perform initialization.	   
"""

# Note : Class Name and Method name can be same.

class Test:
	def Test(self):
		print("Method")

t=Test()   ## Creating Object
t.Test()   ## Calling the Method
Test().Test() ## Creating + calling the method 
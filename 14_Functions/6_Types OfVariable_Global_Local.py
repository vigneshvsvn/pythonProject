"""
Types of Variables in Functional Programming.
1. Global Variables
	Variable outside of Function is call Global Variable

	Need of global Key word.
	1. to make global variable available to the function to skip local Variable.
	2. To Declare global variable directly inside a function.

	globals() --> will return dict of all global value in the Moodule
	
2. Local Variables

"""

a=10        ## a is the global Variable and available for all functions .

def f1():
	print(a)           ## Consider Global Variable as there no local variable name with a

def f2(b):   ## b is local to this function f2 and can't be access outside the function
	print(b)
	print(a)      ## as variable a is not available locally so it will consider global

def f3():
	global a         ## we telling to consider global a instead of   local
	a=a+1            ##  Global Variable will modify 
	print(a)

def f4(a):
	print(a)      ## Local Copy
	print(globals()['a'])      #    global() function used to get global copy of variables with in the Module.
	globals()['a']=12    ##  modified global copy
	print(a)         ## Local Copy


f1()
f2(40)
f3()
f1()
f4(300)
print(a)      ## Printing new global Copy

"""
Constructor Overloading concept not support in Python.

If we are declaring multiple constructor then PVM will consider only latest constructor

"""

class Test:
	def __init__(self):
		print("No Arg Constructor.")

	def	__init__(self,a):
		print("One Arg Constructor.")

	def __init__(self, a,b) :
		print("Two Arg Constructor")

#t=Test()       #  TypeError: Test.__init__() missing 2 required positional arguments: 'a' and 'b'
#t=Test(10)      #  TypeError: Test.__init__() missing 1 required positional argument: 'b'
t=Test(10,20)

## Constructor with  multiple arguments.
class Test1:
	def __init__(self,a=None,b=None,c=None):
		print("Constructor with 0 or 1 or 2 or 3 Arguments.")

Test1()
Test1(10)
Test1(10,20)
Test1(10,20,30)


## Constructor with  Variable length  arguments.

class Test2:
	def __init__(self,*args):
		print("Constructor with  variable Number of Arguments.")

Test2()
Test2(10)
Test2(10,20)
Test2(10,20,30)
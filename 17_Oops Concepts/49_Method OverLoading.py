"""
Method Overloading: Both method in class having same name with different arguments types.

In Python, Method and Constructor Overloading is  not possible.  Python Virtual Machine will consider latest method in the Class.
-  Python is dynamically typed, we can't declare type explicitly for different arguments.

"""

class Test:
	def m1(self):
		print("No Argument Method.")

	def m1(self,x):
		print("One Argument Method.")

	def m1(self,x,y):
		print("Two Argument Method.")

t=Test()
#t.m1()  	#   Test.m1() missing 2 required positional arguments: 'x' and 'y'
#t.m1(10)   #	TypeError: Test.m1() missing 2 required positional arguments: 'x' and 'y'
t.m1(10,20)


## But in Python we can use with  single Method itself by using below way,
class Test1:
	def m1(self,x):
		print(f"{x.__class__.__name__}-Argument Method")

t1=Test1()
t1.m1(10)
t1.m1(10.5)
t1.m1('Vignesh')
t1.m1([1,2,3,4])


## replacement for  Overloading with number of arguments with single Method.
class Test2:
	def m1(self,a=None,b=None,c=None):
		if a is not None and b is not None and c is not None:
			print("Three Argument Method.")
		elif a is not None and b is not None and c is None:
			print("Two Argument method.")
		elif a is not None :
			print("One Argument Method")
		else:
			print("No Argument Method.")

t2=Test2()
t2.m1()
t2.m1(10)
t2.m1(10,20)
t2.m1(10,20,30)

## Variable type Arguemnt

class Test3:
	def m1(self,*args):
		print("Variable Length Argument")
		
t3=Test3()
t3.m1()
t3.m1(10)
t3.m1(10,20)
t3.m1(10,20,30)

"""
Self Variable is a reference Variable always points to Current Object.
	If we want to refer current Object with in the class then we need to use self.
	to declare instance Variable and access instance Variable
	- First argument to constructor and instance method always self implicit variable.
	- At the time of calling constructor or instance method, we don't need to pass self explicitly, Python will take care.
	- self is not python key word,so we can use any name delf or  any name to represent reference variable. But recommend to self as standard.

"""
class Test:
	def __init__(self):          # self is the reference variable to use  with in the class.
		print("Constructor")
		print("Address of Self:",id(self))

	def m1(self,x):
		print("Value of x:",x)


t=Test()   ## outside of class  we can use 't' reference variable for Object.
print("Address of Object t",id(t))
t1=Test()
print("Address of Object t1",id(t1))
t.m1(10)


	
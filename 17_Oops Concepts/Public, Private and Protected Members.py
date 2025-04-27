"""
Access Specifiers:

1. public Members: Any person can use.
If a Member (Method, Variable.. ) is public then we can access anywhere
with in the class or from  outside the class.

By Default, it is Public

2. private Members: Accessible only within the class. Outside of class is not possible.
suntax: __x=10
prefixed with __member

But Using name Mangling we can access

Name Mangling Eg: __y=20  --> Python internally rename  with _Test.__y .
But we should not do it with name mangling.

3. Protected Members:  Access with in the class and outside of class only from Child class.

Syntax: Single Underscore   Eg: _z=40

It's just naming convention and not implemented at language level.

"""
class Test:
	def	__init__(self):
		self.x=10
		self.__y=20     ## Private variable double Underscore
		self._z=40      ## Protected Variable single Underscore
	def __m1(self): ## Private Method
		print("called Private Method")
	
	def m2(self):
		print("Inside Public Method")
		print(self.x)
		self.__m1() ## with in the class we are accessing public members
		print(self.__y)

t=Test()
t.m2()
print(t.x)     ## trying to access outside of class as well.

#t.__m1()      ##  AttributeError: 'Test' object has no attribute '__m1'     Not possible to access private outside of Class.
print(t._Test__y)       ## still using name mangling we can access outside of class.
t._Test__m1()
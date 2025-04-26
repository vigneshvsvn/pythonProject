"""
Way 1:
Syntax: classname.method(self)
B.m1(self)

Way 2:
super(classname,self).method()
super(C,self).m1() 


"""

class A:
	def m1(self):
		print("Class A.")


class B(A) :
	def m1(self) :
		print("Class B.")

class C(B) :
	def m1(self) :
		print("Class C.")

class D(C) :
	def m1(self) :
		print("Class D.")

class E(D) :
	def m1(self) :
		super().m1()      ## This will call parent as per MRO algo. It will call from Class D.
		B.m1(self)        ## Specifically calling B class m1()
		super(C,self).m1()    ## it will call m1() from parent of class C. Not from Class C
		print("Class E.")

e=E()
e.m1()



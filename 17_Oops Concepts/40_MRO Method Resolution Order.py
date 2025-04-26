"""
In Hybrid Inheritance  Method resolution order decided based on MRO algorithm.

It will be Left to Right.

Using classname.mro() we can find the order easily.

"""

class A:
	def m1(self):
		print("I am from Class A.")
	pass
class B(A):
	def m1(self):
		print("I am from Class B.")
	pass
class C(A):
	def m1(self):
		print("I am from Class C.")
	pass
class D(B,C):
	# def m1(self):
	# 	print("I am from Class D.")
	pass

print(A.mro())
print(B.mro())
print(C.mro())
print(D.mro())

d=D()
d.m1()
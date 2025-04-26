class A:
	def m1(self):
		print("I amd from A.")
	pass

class B:
	def m1(self):
		print("I amd from B.")
	pass


class C:
	def m1(self):
		print("I amd from C.")
	pass


class D(A,B):
	def m1(self):
		print("I amd from D.")
	pass

class E(B,C):
	def m1(self):
		print("I amd from E.")
	pass

class F(D,E,C):
	def m1(self):
		print("I amd from F.")
	pass

print(A.mro())
print(B.mro())
print(C.mro())
print(D.mro())
print(E.mro())
print(F.mro())

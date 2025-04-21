class Outer:
	def __init__(self):
		print("Outer Class Object Creation.")

	class Inner:
		def __init__(self):
			print("Inner Class Object Creation.")

		class InnerInner:
			def __init__(self):
				print("Inner Inner Class Object Creation")
			def m1(self):
				print("Nested_inner_inner method")

obj_outer=Outer()
obj_inner=obj_outer.Inner()
obj_inner_inner=obj_inner.InnerInner()
obj_inner_inner.m1()
print()
Outer().Inner().InnerInner().m1()
"""
We can declare a Method inside Method called Nested Methods.

"""
class Test:
	def	m1(self):

		def cal(a,b):
			print("Sum:",a+b)
			print("diff:",a-b)
			print("Product:",a*b)

		cal(10,20)
		cal(100, 200)

Test().m1()
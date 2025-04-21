"""
Variable used to hold value temporary, and it's local to method not accessible outside of Method

"""

class Test:
	@staticmethod
	def average(list1):
		result= (sum(list1)/len(list1) )       ## Result is local Variable
		return result

	@staticmethod
	def wish(name):
		for i in range(1,6):       ## i is temp variable to hold value 
			print("Good Evening:",name)





l1=[10,20,30,40]
print ("Average Value:",int(Test.average(l1)))
Test().wish("Vignesh")
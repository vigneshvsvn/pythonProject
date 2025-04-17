"""
1. Instance Method:
	Inside Method implementation if we are using instance variable that method has to declare as instance Method.
	Any Method first argument is always self to access instance variable.

2. Class Method: If we are using only static or class variable inside the Method called Class Method.

3. Static Method: Inside not using any class variable or instance variable call static Method.
					General Utility Method no where related to class and object.
					It can use local Variables

"""

class Student:
	schoolName='Vsvn PolyTechnic'
	def __init__(self,name,rollnum):
		self.name=name
		self.rollnum=rollnum

	def getStudentInfo(self):        ## Inside method we are tyring to access Instance Variable. This is call Instance Method.
		print("Student Name:",self.name)
		print("Student Roll Number:",self.rollnum)

	@classmethod      ## Decorator to define as class Method
	def getSchoolInfo(cls1):      ## cls is the reference  to class Object of Student. For every class one special Object will be Created. cls is reference to that Class Object.
		print("Student School Name",cls1.schoolName)
		print("Inside Class Method",id(cls1))
		
	@staticmethod       ## Static Method 
	def getSum(a,b):
		return a+b

print("Outside Address of class Student:",id(Student))
s=Student('Vignesh',70)
s.getSchoolInfo()
print(Student.schoolName)
print("Sum is :",Student.getSum(5,10))


		
		
	
		
"""
Places to Declare Static Variable:
	1. Inside class directly but outside any Method   or constructor. (Generally Best place to Declare)
	2. Inside Constructor by using Class name.But  Variable created when we create Object of the class.
	3. Inside Instance Method by using class name
	4. Inside class Method by using Class name or class reference variable
	5. Inside static Method by using class Name
	6. Outside of class by using Class Name

Access Static Variable:
"""
class Student:
	schoolName='VSVN Polytechnic' # static variable declared with in the class but outside of methods and constructor.

	def __init__(self,name,rollnum):
		self.name=name
		self.rollnum=rollnum
		Student.schoolCity='Virudhunagar'     ## static variables inside constructor by using class.

	def display(self):
		Student.department='EEE'       ## static variable inside instance method using class name
		print("Name:",self.name)
		print("Roll Number:",self.rollnum)

	@classmethod
	def displaySchool(cls):
		cls.lab='Digital Lab'
		print(cls.schoolName)
	@staticmethod
	def displayHOD( ):
		Student.hod='Jawahar'
		print(Student.hod)

print(Student.__dict__)
s1=Student("Vingesh",70)
s1.display()
s1.displaySchool()
Student.fav_subject='Digital Electronics'
print(s1.__dict__)    ## schoolName is not part of object variable   as it's static.
print(Student.__dict__)   ## schoolName variable is available  as static variable also called as Class variable.

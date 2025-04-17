"""
In Oops three important term repeatedly used.

1. class
-  Is Blueprint or template or plan or model is called class.
- Class represent data members and behaviour of object.

	Eg: Building plan is the class.

2. object
- An Instance of a Class or physical existence of a class call object.
- Using One class we can create multiple objects.

	Eg: Each building which constructed using  building plan is called object.

3. reference variable.
- variable used to refer an Object.
- By using this variable we can perform required operations on the object.
- Object can have any number of reference variable.

"""

class Student:
	"""
	Doc String:  Description about the class. But it's not Mandatory.

	This Class developed by Vignesh for Learning/Understanding of Oops.
	"""
#### Variable Used as properties
	"""
	Three types of Variable allowed
	1. Instance Variable --> Object Level Variables.
	2. Static Variables --> Class Level Variables.
	3. Local Variable  --> Method level Variables. 
	"""
	def __init__(self,name,rollNum,marks):
		self.name=name
		self.rollNum=rollNum
		self.marks=marks

	def talk(self):
		print("Hello, I am",self.name)
		print("My Roll Num:",self.rollNum)
		print("My Marks:",self.marks)

#### Methods Functions defied inside class called Methods.
	"""
		Three types of Method  allowed,
		1. Instance Methods 
		2. class Methods 
		3. static Methods.
	"""
s1=Student("Vignesh",70,100)
s2=Student("Priya",50,100)

s1.talk()
s2.talk()

#print(Student.__doc__)        To Read Doc string
#help(Student)
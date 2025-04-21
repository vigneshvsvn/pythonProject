"""
Special type of Instance Method.    If we don't know the values at Beginning   then we go for getter and setter.
if know the values then we will go with constructor.
Setter Method:To Set value to instance variable of Object.  Also known as mutator method
	Syntax: def setMarks(self,marks):
			self.marks=marks

Getter:To get value to instance variable of Object.   Also called accessor Method
	Syntax: def getMarks(self):
			return self.marks
"""

class Student:
	def setName(self,name):
		self.name=name
	def setMarks(self,mark):
		self.marks=mark
	def getMarks(self):
		return self.marks
	def getName(self):
		return self.name

n=int(input("Enter Number of Students:"))
students=[]
for i in range(1,n+1):
	s=Student()
	name=input("Enter Student Name:")
	marks=int(input("Enter Marks:"))
	s.setName(name)
	s.setMarks(marks)
	students.append(s)

for each_students in students:
	print("Hello,",each_students.getName())
	print("Your Marks are",each_students.getMarks())
	print()

	
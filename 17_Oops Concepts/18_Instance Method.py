"""
Inside Method implementation if we are using any instance variable. That method called as Instance Method.
	- If the method is instance Method then first argument should be always self which is reference to current Object.
"""
class Student:
	def __init__(self,name,marks):
		self.name=name
		self.marks=marks

	def display(self):
		print("Hi,",self.name)
		print('Your Mark is:',self.marks)

	def grade(self):
		if self.marks>=60:
			print("You got first Grade")
		elif self.marks>= 50:
			print("You got second Grade")
		elif self.marks >=35:
			print("You got third Grade")
		else:
			print("You are failed")

n=int(input("Enter Number of Students:"))
for i in range(1,n+1):
	name=input("Enter Student Name:")
	marks=int(input("Enter Marks:"))
	s=Student(name,marks)
	s.display()
	s.grade()
	print()
	



	



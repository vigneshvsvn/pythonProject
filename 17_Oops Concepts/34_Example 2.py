class Person:
	def __init__(self,name,age):
		self.name=name
		self.age=age

	def eatdrink(self):
		print("Eat Biryani and drink Soup.")


class Employee(Person):
	def __init__(self,name,age,enum,esal):
		# self.name=name
		# self.age=age
		super().__init__(name,age)       ## need to use super(). If we want to call parent class members from child class
		self.enum=enum
		self.esal=esal

	def work(self):
		print("Work:Coding Python Programs.")

	def empInfo(self):
		print("Employee Name:",self.name)
		print("Employee Age:",self.age)
		print("Employee Number:",self.enum)
		print("Employee Salary:",self.esal)

emp=Employee("Vignesh",34,11916,100000)
emp.empInfo()
emp.work()
emp.eatdrink()

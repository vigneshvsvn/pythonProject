class Person:
	def __init__(self,name,age,height,weight):
		self.name=name
		self.age=age
		self.height=height
		self.weight=weight

	def display(self):
		print("Name:",self.name)
		print(("Age:",self.age))
		print("Height:",self.height)
		print("Weight:",self.weight)


class Employee(Person):
	def __init__(self,name,age,height,weight,emp_num,emp_sal):
		super().__init__(name,age,height,weight)
		# self.name = name
		# self.age = age
		# self.height = height
		# self.weight = weight
		self.empNum=emp_num
		self.empSal=emp_sal

	def display(self):
		# print("Name:",self.name)
		# print("Age:",self.age)
		# print("Height:",self.height)
		# print("Weight:",self.weight)
		super().display()
		print("Employee Number:",self.empNum)
		print("Employee Salary:",self.empSal)

e=Employee("Vignesh",34,5.5,76,11916,100000)
e.display()
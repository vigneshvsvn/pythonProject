""""
Inheritance:  WHen we want to extend existing Functionality then go for Inheritance.
Composition: When we just want to use the functionality with out extending then Go for composition.


"""

class Car:
	def	__init__(self,Model,Color):
		self.carModel=Model
		self.color=Color
	def carInfo(self):
		print(f"Print {self.carModel}, Colour is {self.color}.")

class Person:
	def __init__(self,name,age):
		self.name=name
		self.age=age

	def eatdrink(self):
		print("Eat Biryani and drink Soup.")


class Employee(Person):
	def __init__(self,name,age,enum,esal,car):
		# self.name=name
		# self.age=age
		super().__init__(name,age)       ## need to use super(). If we want to call parent class members from child class
		self.enum=enum
		self.esal=esal
		self.car=car

	def work(self):
		print("Work:Coding Python Programs.")

	def empInfo(self):
		print("Employee Name:",self.name)
		print("Employee Age:",self.age)
		print("Employee Number:",self.enum)
		print("Employee Salary:",self.esal)
		self.car.carInfo()

c=Car("Innova",'HCross')
emp=Employee("Vignesh",34,11916,100000,c)
emp.empInfo()
emp.work()
emp.eatdrink()

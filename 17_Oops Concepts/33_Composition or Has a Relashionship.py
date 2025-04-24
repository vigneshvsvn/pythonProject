"""
Using Members of one class into another by using Has a relationship  and is a relation ship
Ways:
1. Has a relation --> Composition
	- create object of required class inside another class.
	- code reusability
	- composition : Compose bigger object with small individual objects
	In our example class Car has a relationship with Engine Class

2. is a relation --> Inheritance

 """
###################### Example  1 #############################
class Engine:
	

	def m1(self):
		print("Engine Specific Functionality..")

class Car:
	def __init__(self,name,model,color):
		self.engine=Engine()      ## Composition  or Has a relationship as we crete object of other class inside car class.
		self.name=name
		self.model=model
		self.color=color

	def m2(self):
		print("Car Required Engine Functionality...")
		self.engine.m1() ## Car is using Engine Class Functionality

	def getinfo(self):
		print(f"Car Name:{self.name}, Car Model:{self.model}, Car Color:{self.color}. ")


class Employee:
	def __init__(self,ename,enum,car):
		self.empName=ename
		self.empNum=enum
		self.empCar=car

	def emp_info(self):
		print(f"Employee Name:{self.empName}")
		self.empCar.getinfo()


car=Car('Innova','Hcross','White')
e= Employee("Vignesh",'11916',car)
e.emp_info()





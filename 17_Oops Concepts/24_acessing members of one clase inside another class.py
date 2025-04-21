"""
Member of one class Members inside another class is possible.


"""
class Employee:
	def __init__(self,e_name,e_num,e_sal):
		self.name=e_name
		self.num=e_num
		self.salary=e_sal

	def display(self):
		print("Employee Name:",self.name)
		print("Employee Num",self.num)
		print("Employee salary",self.salary)

class Manager:
	def updateEmpSal(emp):
		emp.salary=emp.salary+10000
		emp.display()

emp=Employee("Vignesh",70,25000)
Manager.updateEmpSal(emp)


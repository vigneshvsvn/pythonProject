class Employee:
	def __init__(self,emp_num,emp_name,emp_sal,emp_city):
		self.empNumber=emp_num
		self.empName=emp_name
		self.empSalary=emp_sal
		self.empCity=emp_city
	def display(self):
		print (f'empNumber:{self.empNumber}',
			   f'empName:{self.empName}',
			   f'empSalary:{self.empSalary}' ,
			   f'empCity:{self.empCity}'
			   ,sep='\n')
	def __str__(self):
		return f"empNumber:{self.empNumber}\nempName:{self.empName}\nempSalary:{self.empSalary}\nempCity:{self.empCity}"

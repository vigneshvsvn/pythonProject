"""
pickle: Module
Serialization: use dump(object,file) method to convert an object to file.
DeSerialization: use load(file) method to convert a file to Object. It returns Object

refer:
emp.py --> is the employee class.
sender.py --> responsible for serialization.
receiver.py --> responsible for De Serialization.
"""
import pickle


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


e=Employee(1,'Vignesh',100000,'Bangalore')
#print(e)

with open('emp.ser','wb') as f:
	pickle.dump(e,f)               ## serialization

with open('emp.ser','rb') as f:
	emp_obj=pickle.load(f)         ## Deserialization

#emp_obj.display()
print(emp_obj)

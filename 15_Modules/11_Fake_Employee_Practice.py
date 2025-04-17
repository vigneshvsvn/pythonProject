from pickle import PROTO
from random import *

alphas='abcdefghijklmnopqrstuvwxyz'
digit='0123456789'
city=['Chennai','Bangalore','Hyderabad','Pune']
designations=['Software Engineer','LeadSoftware Engineer','Team Lead','Manager','Project Lead']

def emp_name():
	## name should be 3 to 10 chars
	## first should be Capital rest all lowercase
	name=choice(alphas).upper()
	n=randint(2,9)
	for i in range(n):
		name=name+choice(alphas)
	return name

def emp_number():
	# should start with 'E-'  followed by 4 digits
	name='E-'
	for i in range(4):
		name=name+choice(digit)
	return name

def emp_sal():
	## should be float value between 10000 -50000
	return round(uniform(10000,50000),2)

def emp_city():
	## from Hyderabad, chennai, Bangalore, Pune
	return choice(city)

def emp_mob():
	## should contain 10 digits and first number should start with 6|7|8|9  rest can be anything
	number=str(randint(6,9))      ## should be simplified solution by using choice('6789')    it will avoid type conversion to str
	for i in range(9):
		number=number+choice(digit)
	return number

def emp_designation():
	## Softwared Eng, lead SOftwared Eng,Manager, Team Lead , Business Analyst ,,
	return  choice(designations)

def fake_employee():
	print("Employee Name:",emp_name())
	print("Employee Id:",emp_number())
	print("Employee Salaray:",emp_sal())
	print("Employee City",emp_city())
	print("Employee MobileNumber:",emp_mob())
	print("Employee Designation:",emp_designation())


for i in range(1,11):          ## 10 FAKE EMPLOYEE DATA
	print(f"Detail of Employee {i}:",'*'*50)
	fake_employee()
	print()



import pickle,emp

f=open('emp.ser','wb')
while True:
	eno=int(input("Enter Employee Number:"))
	ename=input("Enter Employee Name:")
	esal=float(input("Enter Employee Salary:"))
	ecity=input("Enter Employee Salary:")

	e=emp.Employee(eno,ename,esal,ecity)
	pickle.dump(e,f)

	option=input("Do you want to enter another Employee ? {Yes or No}:")

	if option.lower()=='no':
		break
print("Multiple employee objects serialized.")


	

	
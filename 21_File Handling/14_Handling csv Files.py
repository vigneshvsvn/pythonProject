"""
using inbuilt Module csv.

csv --> comma separated values
"""

import csv

with open('emp.csv','w',newline='') as f:
	writer=csv.writer(f)   ## pointing file object to a writer object to write
	writer.writerow(['Emp_Num','Emp_Name','Emp_Sal','Emp_Add'])
	while True:
		enum=int(input("Enter Employee Number:"))
		ename=input("Enter Employee Name:")
		esal=float(input("Enter Employee Sal:"))
		eaddress=input("Enter Employee address:")
		writer.writerow([enum,ename,esal,eaddress])
		option=input("Do you want to insert one more Record [Yes or No] ? :")

		if option.lower()=='no':
			break

print("Writing data completed.")



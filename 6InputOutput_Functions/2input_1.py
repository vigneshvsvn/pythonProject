emp_id=int(input("Enter Employee id:"))
emp_name=input("Enter Employee Name:")
emp_sal=float(input("Enter Employee Salary"))
emp_city=input("Enter Employee City:")
#emp_married=bool(input("Enter Employee Married status true or false:"))     ### This will not work if we give False, bool() will return False only for '' empty string.
emp_married=eval(input("Enter Employee Married status true or false:"))   ## Use Eval function for type cast string to bool.

print(emp_id,emp_name,emp_sal,emp_city,emp_married)

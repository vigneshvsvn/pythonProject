## Example 1 :
try:
	print("Statement 1")
	print(10/0)
	print("Statement 3")

except ZeroDivisionError as msg:         ## creating object reference to  ZeroDivisionError class for future accessing.  msg is the reference Variable.
	print("Exception Message type:", type(msg))
	print("Exception Class Name:",msg.__class__.__name__)
	print("Description of Exception:",msg)

#Example 2: using Base Exceptions
try:
	x=int(input("Enter Value of X:"))
	y=int(input("Enter Value of y:"))
	print("Result:",x/y)

except BaseException as msg:
	print("Exception Type:",type(msg))
	print("Exception Class:",msg.__class__.__name__)
	print("Description of Exception:",msg)

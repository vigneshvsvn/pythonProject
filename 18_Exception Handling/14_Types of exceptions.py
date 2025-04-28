"""
1. Predefined Exceptions.
- Inbuilt exception raised automatically by PVM when ever particular event Occurs.
Example 1:
	10/0 --> ZeroDivisionError
Example 2:
	x=int('10')
	y=int('Ten') -- ValueError

2. User defined Exceptions.
- Programmer of Developer has to define our Exception. And raise exception when ever something goes Wrong.
when we want to write own exception then we inherit BaseException or Exception or other child exceptions classes.

Generally inherit Exception

"""
from tkinter.font import names


class GVKException(BaseException):
	def __init__(self,msg):
		self.msg=msg


wife_name=input("Enter your Name:")

try:
	if wife_name=='Priya':
		print("Authorized to use Vigesh Account.")
	else:
		raise GVKException(f"{wife_name} is not wife of Vignesh.")
# except GVKException:
# 	print("Please find correct Husband.")
finally:
	print("Thank you..")







	
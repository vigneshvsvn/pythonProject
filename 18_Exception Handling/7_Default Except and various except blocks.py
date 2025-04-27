"""
Default except block: If no except block matched, then  default except block will consider.
	Generally used only to print exception details to console not to Handle  alternative.

syntax:  Must be used at last after that we can't use any other except block,
except:
	   statment
"""

try:
	x=int(input("Enter Value of X:"))
	y=int(input("Enter Value of y:"))
	print("Result:",x/y)

except ZeroDivisionError as msg:
	print("Exception type:",msg.__class__.__name__)
	print("Description of Message:",msg)
except:
	print("Default Exception: Only Integer type of input is allowed.")



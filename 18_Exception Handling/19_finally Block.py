"""
finally, block will always execute at the end of try, except block.     In any case finally block will execute even exception or no exception.

Eg: connection close of Database at the end even though
the Main purpose:  Clean up code (resource reallocation) will be written Finally Block.


"""

print(EOFError.mro())

try:
	x=int(input("Enter Value of X:"))
	y=int(input("Enter Value of y:"))
	print("Result:",x/y)

except ZeroDivisionError as msg:
	print("Exception type:",msg.__class__.__name__)
	print("Description of Message:",msg)
except :
	print("Default Exception: Only Integer type of input is allowed.")
finally:
	print("Finally Block for Clean up code.")
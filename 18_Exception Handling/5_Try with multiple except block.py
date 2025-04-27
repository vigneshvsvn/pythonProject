"""
Multiple except block is possible and recommended to use.
Order of except block is from Top to Bottom until matched block identified.
"""
try:
	x=int(input("Enter Value of X:"))
	y=int(input("Enter Value of y:"))
	print("Result:",x/y)

except ValueError as msg:
	print("Exception type:",msg.__class__.__name__)
	print("Exception Description:",msg)

except ZeroDivisionError as msg1:
	print("Exception type:", msg1.__class__.__name__)
	print("Exception Description:", msg1)

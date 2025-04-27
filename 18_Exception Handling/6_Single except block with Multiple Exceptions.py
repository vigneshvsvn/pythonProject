"""
syntax: except(Exception1,Exception2 ....) as msg
when we have the same handling for multiple exception then go for single except block.
"""

try:
	x=int(input("Enter Value of X:"))
	y=int(input("Enter Value of y:"))
	print("Result:",x/y)

except (ValueError,ZeroDivisionError) as msg:
	print("Exception type:",msg.__class__.__name__)
	print("Exception Description:",msg)

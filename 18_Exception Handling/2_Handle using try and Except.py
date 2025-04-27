"""
The Code which may raise Exception called Risky Code.
For : Risky Code always should handle with exceptions.

In try block, we need to write normal code.
In Except block, we need to write alternative code to handle exception for continue the program for Graceful Termination.

try:
	Risky Code
except:
	Handling Code

"""

print("Hello")
try:
	print(10/0)
except ZeroDivisionError:
	print("Division by Zero Not Possible.")
print("Hi")
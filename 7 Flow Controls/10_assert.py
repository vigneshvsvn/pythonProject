"""
Assertion is one of the method for creating Exception

The assert keyword is used when debugging code.
The assert keyword lets you test if a condition in your code returns True, if not, the program will raise an AssertionError.
You can write a message to be written if the code returns False, check the example below.

syntax : assert expression "Statement to print for false"
"""

num=int(input("Enter number greater than 10: "))
assert num>10, "wrong Number"
print("Your Number is:",num)
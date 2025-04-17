"""
Input is the function to get input from console or user
default is string, if we want we need to typecast

raw_input() only in python 2.x  --> To read end user data always going to provide in the form of string only. type casting is required always.
input() --> Read data from user.  return type is string
"""
# s=input()
# print(s)
# s=input("Enter the Name:")     --> input function will return string.
# print(s)
# i=int(input("Enter a Integer Number:"))
# print(i)


x=input("Enter Input for x:")
y=input("Enter Input for y:")
z=int(input("Enter Input Z:"))
print("x=",x,type(x))
print(int(x)+int(y))          ## To sum we need to type case to int because input() retrun string. If we are not doing then string will concat both value instead of sum.


#########More than one Input
# lst=[x for x in input("Enter Three number separated by space").split()]
# lst=[x for x in input("Enter Three number separated by space").split()]
# print(lst)
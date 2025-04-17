""""
How to find members of Particular Module.
dir() --> Finding members of current module and return list
dir(module_name)  --> to list of all members of specified Module.

help()    --> Will give explanation for Member and it's purpose

"""
import math


a=10
b=20
def add(a,b):
	return a+b

print(dir())
print("*"*50)
print(dir(math))
print("*"*50)
print(help(math))

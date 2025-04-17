""""
Bitwise: We have to apply bitwise.
applicable only for Int type and Boolean Type
Example : (4=100 & 5=101) --> 100
& --> bitwise and
| --> bitwise or
^ --> Bitwise XOr    odd number of True then True else false
~ --> Bitwise Complement operator
<< --> Bitwise left shift operator
>> --> Bit wise right shift operator
"""
a=5
b=4
print("a=",bin(a))
print("b=",bin(b))
print("a&b:",a&b,bin(a&b))
print("a|b:",a|b,bin(a|b))
print("a^b:",a^b,bin(a^b))
print("~b:",~b,bin(~b))   ###

######### Boolean type
print(True & False)
print(True | False)
print(True ^ False)


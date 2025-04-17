"""
a=10    --> It allocate memory and store 10
b=10    --> As 10 already in memory b will use same memory location
b=14    --> New Memory will allocate for 14 and point b to that new memory location

"""
a=10
b=10
print(id(a))
print(id(b))
print(a is b)
b=14
print(a is b)
print(id(a))
print(id(b))
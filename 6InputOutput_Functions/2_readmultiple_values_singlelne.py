"""
List Comprehension  and unpacking of list.

input("Enter two number:").split()     --> split string based on space and it return list

"""


a,b=[int(x) for x in input("Enter two number:").split()  ]
print(a+b)

x,y,z=[float(i) for i in  input("Enter 3 Number with comma separation").split(',')]
print(x+y+z)
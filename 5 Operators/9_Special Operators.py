""""
1. Identity Operators  -->
(is) and (is not) are identity Operator  

2. Membership operator
in operator
and not in
- where the value is member of the sequence or not

"""
a=10
b=20
c=b

print("a is b",a is b)
print("a is not  b",a is not b)
print("c is b",c is b)
print("c is not  b",c is not b)

l1=[10,20,30,40]
l2=[10,20,30,40]
print(l1, id(l1),l2, id(l2))
print("List1 is list2:",l1 is l2)
print("Content  of l1 and l2 are Equal? ", l1==l2)

print("40 is member in list 1 ?", 40 in l1)

s="Learning Python is Easy"

print("V is not in the String s ?", 'V'  in s)
print("Python is  in the String s ?", 'Python'  in s)

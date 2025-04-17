"""
len(lst) --> Inbuilt Python  Function
t.count() --> Number of occurrence of element.
t.index() --> List class specific Method.

"""

t=(10,20,30,10,30,20,10)
print(len(t))   ## return int type with length of List.
print(t.count(10))           ##         tuple class  specific Method
print(t.count(50))           ## return 0 if not found

print(t.index(20))  # return index of first occurrence of element
print(t.index(10,2,5))       #
if 5 in t:
	print(t.index(5))       ## Value error, If not found then throw error. We need to check value available or not in the list before using index method.

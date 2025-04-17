"""
len(lst) --> Inbuilt Python  Function
lst.count() --> Number of occurrence of element.
lst.index() --> List class specific Method.

"""

lst=[10,20,30,10,30,20,10]
print(len(lst))   ## return int type with length of List.
print(lst.count(10))           ##          List specific Method
print(lst.count(50))           ## return 0 if not found

print(lst.index(20))  # return first occurrence
print(lst.index(10,2,5))       #
if 5 in lst:
	print(lst.index(5))       ## Value error, If not found then throw error. We need to check value available or not in the list before using index method.

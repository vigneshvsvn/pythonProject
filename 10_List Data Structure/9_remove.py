"""
To remove specified element from the list.
Many Loopholes:
- only first occurrence  will be removed
- if element not available in the list then we will get value error. So need to check element availability before usnig it.

"""

l=[10,20,10,20,40]
print(l)
l.remove(40)
print(l)
l.remove(10)   ## Only First Occurrence will be removed
print(l)
l=[10,20,10,20,40]

#########How to remove all     Occurrence

x=int(input("Enter element to remove:"))
while True:
	if x in l:
		l.remove(x)
	else:
		break

print("After Removal: ",l)

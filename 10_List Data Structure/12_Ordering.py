"""
1.  l.reverse()
  - Reversing order of elements in the list.
  - list specific method
2. reversed()
	- python specific method, returns revered_iterator --> need to convert to list
	- it will create new object not modify anything on existing object.
3. l.sort() --> Default natural sorting and it's list specific method.
				For Number it's ascending order
				For String it's alphabetical Order
				In existing list object itself it will do sort.
4.sorted()  --> Python specific  function
				- New list will created and return iterable

"""
l=[10,20,30,40,9]
print(l)
l.reverse()
print(l)
r=reversed(l)
rev=list(r)
print(rev)
print(l)
l.sort()
print("After Sorting",l)            ## natural SOrt
l.sort(reverse=True)
print(l)

new_list=sorted(l)
print(new_list)

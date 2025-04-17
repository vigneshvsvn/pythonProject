"""
pop() --> to remove last element in the list. if we dont pass  any parameter.  and retrun the poped elemet
		- When list is empty still if are using pop. Then we will get index error.

pop(index) --> Remove the element of given Index. and retunt the element
				If Index is out of range then it will give index error.
"""
l=[20,30,45,79,97,23]
print(l)
a=l.pop()
print(l)
print(a)


#########How to remove element of particular Index
a=l.pop(2)         ## remove element in the index 2 from the list
print(l)
print(a)

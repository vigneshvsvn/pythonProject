"""
aliasing --> calling same object with multiple references.
cloning  --> Create new object
	- using slice operator
	- list.copy() class method
"""
from time import perf_counter

l1=[10,20,30,40]
l2=l1        ##  aliasing address will be same. Now two reference points to same object. So any change on one reference the it will impact other.
print("Address of l1",id(l1),l1)
print("Address of l2",id(l2),l2)
l2[1]=30
print(l1,l2)      ## can see both are modified if we do aliasing.

l1=[10,20,30,40]
l2=l1[::] ## Duplicate object created using cloning.
print(l1,l2)
l3=l1.copy() ## new object Created

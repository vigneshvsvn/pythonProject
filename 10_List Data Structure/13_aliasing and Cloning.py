"""
aliasing --> calling same object with multiple references.
cloning  --> Create new object
	- using slice operator
	- list.copy() class method  -->  Shallow Copy


Deep Cloning: Complete copy
object will be cloned include a nested object inside it.
copy.deepcopy(l4) using copy module using deepcopy function.

If we have to copy nested objects, then go for deep cloning.

Shallow Cloning: --> Partial Copy
If an original object contains any nested object then In cloned copy for nested object separate copy will not happen.
Only duplicate reference will be created.

copy.copy(l4),list.copy(),

If we are not having a nested object then go for shallow cloning.

"""
from pickle import PROTO
from time import perf_counter
import copy

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

################# DeepCloning and Shallow Cloning ############
l4=[10,20,[30,40],50]
l5=l4.copy()     ## Shallow Copy
l6=copy.copy(l4) ## Shallow Copy
l7=copy.deepcopy(l4) ## Deep Copy
print("After Cloning:")
print('l4:',l4)
print('L5:',l5)
print('L6:',l6)
print('L7:',l7)
l5[0]=777
l5[2][0]=999     # when we are coping, a nested object will create a duplicate reference variable, Not a Duplicate Object called shallow copy.
l6[2][0]=888
l7[2][0]=222
print("After Modification on L5:")
print('l4:',l4)
print('L5:',l5)
print('L6:',l6)
print('L7:',l7)


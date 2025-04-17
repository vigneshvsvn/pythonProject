"""
lst.append() --> used to add at end of the list.
lst.insert() --> used add at specified position.

"""
from os import lstat

l=[]
l.append(10)
l.append(20)
l.append(30)
print(l)

lst=[]
for each_number in range(1,101):
	 if each_number%10==0:
		 lst.append(each_number)
print(lst)
lst.insert(1,11)      ## Element 11 inserted on 1st Index
print(lst)
lst.insert(100,101)    ## 100 index is not available in the list. So by default it will add at end.
print(lst)
lst.insert(-100,9)  ##     -100 index is not available so it will add at beginning of the list 
print(lst)


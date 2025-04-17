"""
eval will evaluate the data return typecast it automatically .
eval(x)
[1,2,4,5,6]

Alternative to all type cast eg: int(x), float (x), string(x) ---> eval(x)
"""
## Way 1:
lst1=eval(input("Enter List of Elements"))            ## eval will cast according to input from user here
print(lst1)
lst2=[]
for each_value in lst1:
	if each_value not in lst2:
		lst2.append(each_value)
print(lst2)

#Easy Way:
##lst1=eval(input("Enter List of Elements"))
print("After removing Duplicate Using Set",set(lst1))


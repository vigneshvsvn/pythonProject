"""
To add all elements of given sequence to the list.
 - Add multiple element in the sequence  individually.

"""

l1= ['Chicken','Mutton','Fish']
l2= ['Prawn','Turkey','Duck']
print(l1,'\n',l2)
l1.extend(l2)
print(l1)

lst1=[1,2,3]
lst2=[4,5,6]
#lst1.append(lst2)     ## [1, 2, 3, [4, 5, 6]]  --> lst2 considered as single object(list) if we do append().
lst1.extend(lst2)      ## [1, 2, 3, 4, 5, 6]     --> lst2 elements considered as individual element and extended to existing list.
print(lst1)


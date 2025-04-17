"""
1. == and != --> Equality operator
	== return True only when following satisfy
	- Number of Element must be same.
	- The Order of Elements must be same
	- Content of element must be same with case

2. Relational Operators.
<, <=,>,>=
	-   it will be for Content element by element.  Start with first element, if it not able to decide then go for next element comparison.
	- If it strings

3. Membership in and not in
"""
l1=('Dog','Cat','Rat')
l2=('Dog','Cat','Rat')
l3=('DOG','CAT','RAT')
l4=('Cat','Dog','Rat')
print(l1==l2)      ## True as it's exactly same.
print(l1==l3)
print(l1==l4)
print(l1!=l4)      ## True as l1 is not equal to l4
lst1=(10,20,30,40)
lst2=(50,60)
print(lst1<lst2)       ##  10< 50   --> True
print(lst1<=lst2)      ##  10<=50   --> True
print(lst1>lst2)       ##  10>50     --> False
print(lst1>=lst2)      ## 10>= 50    --> False

print(10 in lst1)
print(10 not in lst1)
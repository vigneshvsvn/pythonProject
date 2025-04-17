"""
FIlter() will not manipulate/modify elements , so if we want to modify then need to go for map().
Apply some  function and generate new element/value and create new sequence with new value.

If above is the requirement then go for map().

 Eg:
list --> 10 elements
map  output -->   10 elements should generate

For Each element new element will be generated

It can be used for multiple sequences.

"""

l=[1,2,3,4,5]

print("Actual List:",l)

## With out map
def squreit(n):
	return n**2

l1=list(map(squreit,l))        ## return map object need to type cast if we want to get as sequence
print("Squreit List",l1)

## Using Lamda
l2=list(map(lambda n: n**2,l))
print("Squreit Lamda:",l2)

## using multiple sequences also applicable
liat1=[1,2,3,4,5,6]
list2=[5,10,20,30,40]
list3=list(map(lambda x,y:x*y,liat1,list2))   ## If number of length not matched, excess element will be ignored.
print("List1",liat1)
print("List2",list2)
print("Product of two sequences List 1 and List2: ",list3)




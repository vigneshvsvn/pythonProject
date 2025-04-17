"""
When to go for Set:
* We represent group   unique object as single entity where order is not important.
   - Means Duplicate not allowed
   - Order of insertion not preserved. As there is no order Indexing and slicing are not applicable
* objects with in {} consider as set
* Heterogeneous   Objects are allowed
* Mutable
* Hashable
* Union, Intersection, difference, symmetric difference  .... Mathematical operation  allowed
* empty set should be set(). We can't use {} as python give priority to Dictionary   type as it's commonly used than set.



"""
s=set()       ## Creating empty set Object
print(s)

s.add(10)           ## possible to add as it's mutable
s.add(20)
s.add(65)
s.add("Vignesh")
s.add((10,20))
s.add(20)          ## Duplicate values will be ignored, there will not be any error 
#s.add([45,65])    ## TypeError: unhashable type: 'list'         List is not allowed
#print(s[0])       ## TypeError: 'set' object is not subscriptable, means index/ slice is not allowed as it's not having   order.
s.remove(65)       ## remove is possible in set as it's mutable
print(s)


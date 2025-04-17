"""
- To hold group of values/entities we can use List.
- Order is important and  Duplicate allowed then go for list
- HETEROGENEOUS -- Different data types are allowed
- Indexing concept is applicable
- slicing is allowed
- repetitions allowed 
- list is growable in nature (we can add using append() and remove using remove())
- Liat is mutable, we can change the content of the element or object.
- list require more memory compare to tuple
- compare to tuple performance is less as list is mutable/changeable 
"""

lst=[10,20,"Vignesh",99.5,-10]              ### Square bracket need to use to define list and it can be any datatype (HETEROGENEOUS -- Different type )
lst1=[]  ## empty list
print(lst)
print(lst1)

### We can perform Indexing, Slicing and repetitions
print(lst[3])          ##Indexing
print(lst[3:5])        ## Slicing
print((lst*2))         ## repetitions

print(len(lst))

######### Add , Remove elements from the list

lst.append(40)    ## Added at end of the list
lst.append(10)
print(lst)

lst.remove(10)    ## Remove First occurrence  by value
print(lst)

del(lst[1])       ## Remove by Index we need to use del function in python
print(lst)

###print(lst.clear())           ## TO Clear all elements in the list
##print(lst)

print(max(lst))               ## To Print Maximum element value in the list
print(min(lst))               ## To Print Minimum element  value in the list

##lst.insert(3,"Vignesh")     ## insert element to list Here we are adding element "Vignesh" on Index 3
print(lst)

##########Sort List 
lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)
""" just like List but can't be modified Immutable. So it's like readonly version of list.
- Order is important and  Duplicate allowed then go for list
- HETEROGENEOUS -- Different data types are allowed
- Indexing concept is applicable
- slicing is allowed
- repetitions allowed
- list is growable in nature (we can add using append() and remove using remove())
- Less memory required compare to list
- faster access of tuple as it's read only so performance is more.
single element tuple should end with , else it will not treat as tuple       Eg: tpl=(1,)  if we are not giving , then it will consider as integer

"""

tpl=(1,3,6,	6,10,-20,"Vignesh")
tpl_empty=()
tpl_1argument=(1,)
print(type(tpl))
print(type(tpl_empty))
print(type(tpl_1argument))
print(tpl)
print(tpl*2)       		## Repetition
print(tpl.count(6))     ## Count Elements values
print(tpl.index(-20))
print(tpl[5])


#########     List to Tuple

lst=[3,5,6,7]
tpl1=tuple(lst)
print(type(tpl1),tpl1)

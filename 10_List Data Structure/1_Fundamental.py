"""
If we want to represent group objects as Single Entity. Then we need to GO for Collection Data type(List,tuple,set,Dictionary,bytes,bytearray....).
1. List
When to go for List:
- Order need to preserve
- duplicate allowed
- list=[] is empty list
- To add element List.append
- Heterogeneous
- List is Dynamic --> can add/remove element.
	To increase  --> append(),insert(),extend()
	To Decrease --> remove(),pop(),clear()
- Mutable
- UnHashable (hash search algorithm  not possible)
- can't be used inside set,
- can't be used in Dictionary as Key but can be used in Value

How to Create.
1. lst=[]
2. lst1=[5,8,"vignesh",98]
3. user_input=eval(input("Enter List:"))   from user get the list.
4. using list() function
	s="Vignesh"
	lst3=list(s)
5. using split() Method
	s1 = "Learning Python is Easy"
	lst5 = s1.split(' ')
"""
from  collections import  Hashable
from collections.abc import Collection

lst=[]     ## Empty list Created
print(type(lst))
##print(isinstance(lst,collections.Hashable))     ## not available after python 3.8
lst1=[5,8,"vignesh",98] ## If we know the data then we can assign it directly.
print(lst1)
lst.append(10)
lst.append("Vignesh")
lst.append(30.0)
lst.append(True)
lst.append(10)
print(lst)
lst[0]=15    ## Mutable, So  we can change the existing values	
print(lst)

user_input=eval(input("Enter List:"))  ## Create list from user
print(user_input)

s="Vignesh"
lst3=list(s)     ## Using list() method we can convert/create new list
print(lst3)
lst4=list(range(1,10,2))
print(lst4)

s1 = "Learning Python is Easy"
lst5 = s1.split(' ')
## using split option we can create list. It's applicable for String.
print(lst5)

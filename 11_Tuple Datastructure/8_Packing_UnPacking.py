"""
Packing : Packing multiple variables/value  in to a tuple,list,set.
unpacking: unpack tuple/list/set to multiple variables.

Note : Length of tuple  and number of variables should   be matched.
"""
a=2
b=20
c=87
d=99
tup=(a,b,c,d)      ## Pack to tuple () or without ()
lst=[a,b,c,d]      ## Pack to list  []

print(type(tup),tup)
print(type(lst),lst)

w,x,y,z=tup          ## unpack tuple and assign to variables
print(w,x,y,z)

e,f,*g=tup     ## *g --> variable length argument. e and f will be assigned individuality and remaining will assigned to b as List
print(e,f,g)
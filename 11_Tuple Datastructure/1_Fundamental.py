"""
Tuple :
      same as list but immutable/can't be changed. THe content is fixed the go for Tuple.   Represent tuple using ()
      - Order preserved
      - duplicate allowed
      - Heterogeneous objects are allowed
      - index allowed  as order is preserved else not possible.
      - slicing allowed
      -(1,) if tuple has only one element then it need to end with ','  else it will not consider as tuple.
      - is hashtable so it uses hash search algorithm. So search in tuple is fast. Performance is more compare to list.
"""
k=(1,2,3,4,5,6)
l=1,2,3,4,5          ## with our () it will consider as tuple.
m=(1,)                ## single element tuple should end with ','
n=2,
print(type(k),type(l),type(m),type(n))
print(k,l,m,n)
print(k[0],l[0]) ## indexing allowed
print(k[1::2])    ## Slicing allowed

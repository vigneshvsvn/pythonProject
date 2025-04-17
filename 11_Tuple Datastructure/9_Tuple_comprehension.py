"""
   `Easy way of creating Tuple
   - Concise way of creating Tuple,
   Compression is not applicable  directly for tuple. As it will return generator Object not tuple object, so we need to cast using tuple()

Note: We need to explicitly cast to tuple. 
"""


t= tuple(( x*x  for x in range(1,10)))
print(t)
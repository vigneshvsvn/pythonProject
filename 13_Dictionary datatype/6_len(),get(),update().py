"""
len()     --> Return number of items, that is key value pairs
d.get()   --> It return value associated with key. Even specified not availble we will not get any error. Just get retrun as None.
d1.update(d2) --> all Key values of d2 will be added to d1.   If duplicate are there then it will update to new value.
"""

d={1:'a',2:'b',3:'c',4:'d'}
d2={5:'a',6:'b',7:'c',8:'d'}
print(d)
print("Len:",len(d))
print(d.get(1))
print(d.get(100))  ## if not available then it will return None
print(d.get(d.get(100),"NotAvailable"))      ## if key not available then return customized default value.

d.update(d2)
print(d)




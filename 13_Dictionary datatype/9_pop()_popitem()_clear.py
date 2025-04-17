"""
d.pop(key) --> Removes item associated with specified key and reruns corresponding value.
				- if specified key is not available then we will get key error
d.pop(key,value) --> Removes item associated with specified key and reruns corresponding value.
						if specified key is not available then return given value instead of error.
d.popitem()  --> remove arbitrary/random  key value pair.
				 return item(key,value) as tuple
				 If Dictionary is empty then if try to pop then we will get KeyError: 'popitem(): dictionary is empty'
d.clear()  --> Remove all Key valye pair in the dictionary

"""

d1={100:'A',200:'B',300:'C',400:'D'}
print(d1)
print("Remove key 300 and it's value was ",d1.pop(300))
print(d1)
print(d1.pop(700,"Given Key not available"))
print(d1.popitem())
print(d1)
print(d1.popitem())
print(d1.popitem())
print(d1)
d1={100:'A',200:'B',300:'C',400:'D'}
print(d1)
d1.clear()
print(d1)
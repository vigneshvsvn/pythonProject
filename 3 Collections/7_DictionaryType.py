"""
- group of objects as Key Value pair then need to go for dict data type.
- {key1:value2, key2:value2 .....}
- commonly used datatype in python
- order not applicable, order is based on hashcode of object
- no duplicates key are allowed
- value can be allowed
- As order is not there so Indexing, slicing are not allowed.
It 's similar to Map concept in Java.


"""

dict={
	1:"vignesh",
	2:"Priya" ,
	3:"Privika",
	4:"?"
}
print(type(dict),dict)
print(type(dict.items()),dict.items())
print(type(dict.keys()),dict.keys())
print(type(dict.values()),dict.values())

del dict[4]        ## To Delete we need to use python functions
print(dict)

########## To add to dictionary Eg: dict_empty[100]='police'   --> d[key]=value
dict_empty={}                      ## empty dict
dict_empty[100]='police'
print(dict_empty)





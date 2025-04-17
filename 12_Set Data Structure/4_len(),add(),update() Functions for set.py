""""
len() --> In Built functions in python not class methods
s.add() --> class specific Method. where as in list append() was used. As we dont have Order we have use add() for set.
		--> Used for Individual Object
s.update  --> To add multiple items to the set. But it should be iterable object.

add() vs update()
1. add() is for individual element to set. update() used to add multiple elements
2. add() only arguments , Update() any number for argument but it should be iterable


"""


s1={1,2,3,45,67,34,678,12}
s2={44,33,22}
print("Length of s1:",len(s1),s1)
s1.add(50)
print(s1)
s1.update(s2)     ## used to update multiple values by using iterable (list,range,string , tuple ..)
print(s1)
s1.update("Vingesh")
print(s1)
s1.update('priya','prvika')
print(s1)


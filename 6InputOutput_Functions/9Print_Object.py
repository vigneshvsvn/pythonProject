"""
print can take any type of Object. It's not mandatory of string. It accepts (list, tuple ....)

print statement with replacement operator {}.
"""
l=[10,20,30]
t=(10,20,30)
print(l)
print(t)
name="vignesh"
age=30

print("Hello {} your age is {}.".format(name,age))     #### replacement operator {} with .format        ## old way frequently used 

print("Hello {1} your age is {0}.".format(age,name))     #### replacement operator {} with .format with Index  it's very rare usage


print(f"Hello {name} your age is {age}")                         ###    New commonly used approach

"""
formatted string 
%i --> signed decimal value 
%d --> signed decimal value
%f --> float value 
%s --> string,and any other type list, tuple, set ...

syntax: print("formatted string"%(variable list ))

More powerful than replacement operator.  Example : f=12.39576  we can format required digits using %.2f 
"""
print("hello %s and your age is %i"%(name,age))
marks=[99,50,75]
average=  (99 + 50 + 75)/3
print("hello %s and marks list is %s, your average %f" %(name,marks,average))
print("hello %s and marks list is %s, your average %.2f" %(name,marks,average))     ## formatted float to 2 digit after decimal. In replacement it's not possible.





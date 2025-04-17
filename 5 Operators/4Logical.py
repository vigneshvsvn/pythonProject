
"""
and
or
not
"""

x,y=20,30

#### Boolean Type 
print(x==20 and y==31)      ## Both arguements are True then true
print(x==20 or y==31)       ## atleast one arguemnt is True then True else False
print(not(x==20 or y==31))   ## Complement Not True means True , Not False Means True

uname='Vignesh'
Password='abc@123'
user_name=input("Enter User Name:")
user_password=input("Enter your Password:")
if (uname.lower() == user_name.lower()):
	if(Password==user_password):
		print("Valid User")
	print("Invalid Password")
else:
	print("Invalid User Name...")


#### Non-Boolean Logical operations          Output never be Boolean , out put might be x or y 
""""
empty list,str, tuple,dict treated as False 
0 means False 
non-Zero Means True 

Result will be always x or y based on below.

And Operator:  (x and y) (10 and 20)
if x evaluate True then result is y    --> 20
if X evaluate False then result is x   

or operator:    (x or y)    (10 or 20)                   
if x evaluate True then result is x
if X evaluate False then result is y

not operator:
result is always Boolean.

"""

print(0 and '')

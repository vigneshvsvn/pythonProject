"""
In Python function can return multiple values from a function. In Other languages it's not there.

"""

def sum_sub(a,b):
	sum=a+b
	sub=a-b
	return sum,sub      ## Return multiple value as tuple  

tup=sum_sub(20,15)     ## it will tuple
sum,diff=   sum_sub(20,15)   ## unpack two values in list to two variable             
print(tup,sum,diff)


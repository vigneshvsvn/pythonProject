"""
1. Positional Arguments  :
	arguments which are passing to the function in the correct positional Arguments.
	If interchange position  results will vary
	number of argument and order of arguments should match
2. Key Word Arguments
	- passing arguments by Keyword of parameter  itself. We Can follow any order but number of  arguments should match.
	- Most commonly used and it's not there in Java.

## Both Keyword and positional Argument can be used in parallel.
But First Position and then need to Key word argument   else we will   get Syntax error.

3. Default Arguments
 def wish(name='Guest'):  --> If we are not passing any argument then it will consider as 'Guest' as default.
 								Else it considers default value.
Note: Default arguments should be at the Last
def wish(name,msg):           	
	pass
def wish(name='Guest',msg='Good Morning'):
	pass
def wish(name,msg='Good Morning'):
	pass
Error :
def wish(name='Guest',msg):   ### not Valid as After Default argument it's  not to have non default.
	pass

4. Variable Length Arguments
Pass any number of arguments to the function.
def f1(*variable_name):
	variable_name will consider as tuple


"""
def f1(a,b):   ## call as formal parameter
	print(a+b)

def wish(name='Guest'):
	print("Hello",name,"How are you")

def f2(*n):
	print(n,type(n))

def sum(*n):
	sum=0
	for each in n:
		sum=sum+each
	print("sum is :",sum)

def f3(x,*n):
	print(x)
	print(n)

def f4(*n,x):            ## X should called as key word arguments
	print(x)
	print(n)

##def f5(*n,*m):   Multiple variable length arguments not allowed.
##	pass

#### 1. Positional Arguments

f1(10,20)     ## Actual Arguments.
##f1(10)        TypeError: f1() missing 1 required positional argument: 'b'
f1(20,10)


## 2. Key Word Arguments

f1(a=200,b=100)   ##   We explicitly  mentioned key word for arguments. So order is not important. But Number of argument should match.
f1(b=100,a=200)

## Position + Keyword argument Together					## Both Keyword and positional Argument can be used in parallel.  But First Position and then need to Key word argument
f1(200,b=100)         ## Valid as position arguments passed first before Keyword Arguments
##f1(a=200,100)          SyntaxError: positional argument follows keyword argument

###3. Default Arguments
wish("vignesh")      ## here i am passing value, so it will consider given value
wish()               ## Here i have not passed any value. So it will consider default value in the Function parameter

##4. Variable Length Arguments
f2()
f2(10)
f2(10,20,30)

sum()
sum(10)
sum(10,20,30)

f3(10,20,30,40,50)
f4(10,20,30,40,50,x=60)

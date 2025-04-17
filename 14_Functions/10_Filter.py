"""
- Only to take/filter required things or data.
  filter object from the given sequence using conditions.

  syntax:
  filter(function,sequence)       ## Two arguments
  									1. function is responsible for doing check from the given sequence.
  									2. sequence
	all values in sequence will be passed to function. If function return True then it will add to output. Else it will filter.

Eg:
list --> 10 elements
filter output -->   <=10 elements based on filter logic

"""

l=[0,1,2,3,4,5,6,7,8,9,10]

def isEven(n):
	if n%2 ==0:
		return True
	else:
		return False
## with user defined function example
newFilterList=list(filter(isEven,l))   ## return type is filter object not a list. So Explicitly we need  cast if required.
print( newFilterList)

# Example with lamda
filtererLambda=filter(lambda n: n % 2 == 0, l)    ## using Lamda function without using user defied function.
print(list(filtererLambda))



"""
reduce() is not python inbuilt module. It's there in functools module. So we need to import it explicitly 

reduce() --> reduce multiple/sequence of  elements to single value
if input contains 10 elements then output contains  only one element.

Eg: if we want to sum, min, max like aggregate to single value. then we need to use reduce()


"""
from functools import reduce

l=[10,20,30,40,50]
sum=reduce(lambda x,y:x+y,l)
print(sum)


## sum of first 100 Numbers
print("sum of first 100 numbers",reduce(lambda x,y:x+y,range(1,101)))
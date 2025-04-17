"""
n=3
   *
  * *
 * * *
* * * *


"""
n=15
for i in range(n):
	print((" "*(n-i-1))+('* '*(i+1)))

####Inverted Pyramid
for i in range(n):
	print((" "*(i))+('* '*(n-i)))
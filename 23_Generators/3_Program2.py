"""To Generator Count Down with provided max value"""
from time import sleep
## CountDown
def coundownGenerator(n):
	while n>=0:
		yield n
		n=n-1

g=coundownGenerator(10)
for x in g:
	#sleep(1)
	print(x)

print('##########Fibonacci Number##########')
"""
sum of previous two number call fibonacci Number.
0,1,1,2,3,5,8,13
"""

def fibonacciGenerator():
	a,b=0,1
	while True:
		yield a
		a,b=b,a+b
g=fibonacciGenerator()

for x in g:
	if x <=10:
		print(x,end=',')
	else:
		break
		

	




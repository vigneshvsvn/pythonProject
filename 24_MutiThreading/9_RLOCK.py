""""
problem with simple lock:
if same thread wants to acquire lock again, it's not possible even though the same thread was an owner of existing acquiring.


Why RLock:
ReentrantLock : It will maintain owner information,
				- can track of recursion and release counts
				- only an owner of lock can acquire multiple times.
				- number of acquire and release shuld be same

"""

import time
from threading import *

#l=Lock()
l=RLock()
def factorial(n):
	l.acquire()
	if n==0:
		result=1
	else:
		result=n*factorial(n-1)      ## Same thread is going to lock again as part of recursive, which is not possible in basic lock. So we need to go for RLock
	l.release()
	return result

def  results(n):
	print(f'Factorial  of {n} is {factorial(n)}')


t1=Thread(target=results,args=(5,))
t2=Thread(target=results,args=(4,))

t1.start()
t2.start()


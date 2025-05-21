""""
Lock/RLock --> at time only one thread access lock or Rlock.

semaphore --> used to limit the access to the shared resources with limited capacity.
s=Semaphore(counter)
by default counter will be 1
- acquired and release count need not be matched

BouncedSemaphore()   -->
 If we want to acquire and release count to match then we need to go for BoundedSemaphore
 - If it's not matching it will stop.
"""
import time
from threading import *

l=Semaphore(4) ## 2 means two thread can acquire lock, when third thread comes then it has to wait

def wish(name):
	l.acquire()
	print(f"{current_thread().name} is locking")
	for i in range(5):
		print("Good Morning:",end='')
		time.sleep(2)
		print(name)
	l.release()
	print(f"{current_thread( ).name} released")

t1=Thread(target=wish,args=('Sachin',),name='Sachin Thread')
t2=Thread(target=wish,args=('Ganguly',),name='Ganguly Thread')
t3=Thread(target=wish,args=('Dhoni',),name='Dhoni Thread')
t4=Thread(target=wish,args=('Dravid',),name='Dravid Thread')
t5=Thread(target=wish,args=('Kapil',),name='Kapil Thread')
t6=Thread(target=wish,args=('Yuvraj',),name='Yuvraj Thread')
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
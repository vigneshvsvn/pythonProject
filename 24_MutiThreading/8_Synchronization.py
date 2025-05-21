"""
Maybe a change of inconsistency problem where we are running in parallel.

Eg: Booking ticket. 4 tickets available, If 1000 threads are tying to book so only one person to book/write at a time, For this we need to use synchronization.

To avoid race condition, we need to go for synchronization concept

synchronization means only one thread at time for that piece of code.

Lock:
- most fundamental concept provided by Threading concept.
how to lock and unlock
l=Lock() ## Create lock Object

l.acquire() # Create lock
l.release() # release lock

RLock
Semaphore

"""
import time
from threading import *

l=Lock()

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
t1.start()
t2.start()
t3.start()
t4.start()
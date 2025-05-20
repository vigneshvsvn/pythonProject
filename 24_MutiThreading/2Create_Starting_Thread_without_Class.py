"""
For evey thread separate job is defined.
The main purpose of thread is to execute the corresponding job by starting it.
Once jobs are completed, automatically, thread will terminate.

1. Define some Job for Thread.
2. Create that Thread.
3. Start the Thread.

"""
import time
from threading import Thread, current_thread


def display1():
	for i in range(10):
		print('Samantha.',current_thread().name)

def display2(name):
	for i in range(10):
		print(f'{name}',current_thread().name)


display_thread1=Thread(target=display1)     ## Creating thread to execute display() Function.  Main Thread Creates child thread Object
display_thread2=Thread(target=display2,args=('shreya',))    ## pass arguments in the form of tuple , so for single argument with , at end as tuple
display_thread3=Thread(target=display2,args=('Kajol',))

display_thread1.start()  ## Main Thread Starting child Thread display_thread
display_thread2.start()
display_thread3.start()

for i in range(10):
	print('Vignesh. Executed by',current_thread().name)





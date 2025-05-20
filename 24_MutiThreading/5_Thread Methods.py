"""

ident --> used to identify the id of current Thread.
active_count() --> Number of active threads currently running.  return int type
enumerate --> To get current executing threads objects. return list of active thread objects.
is_alive() --> To check thread is alive or ended.   Return True or False
join() --> If a thread wants to wait until complete another job or Thread.
"""
import time
from threading import *


def display():
	print(f"{current_thread().name} Thread started.")
	time.sleep(3)
	print(f"{current_thread( ).name} Thread Ended.")

# To check number of active Threads
print("Nuber of Active Threads",active_count())
t1=Thread(target=display,name='Child1')
t1.start()
t2=Thread(target=display,name='Child2')
t2.start()
t3=Thread(target=display,name='Child3')
t3.start()

print("Nuber of Active Threads",active_count())

## enumerate used to get list of current threads
curentObjectes=enumerate()
print(curentObjectes)

## To Check Thread is Alive or not
print(f"{t1.name} is Alive? {t1.is_alive()} " )
print('Main Thread identification Number:',current_thread().ident)

for threads in curentObjectes:
	print(f"Name:{threads.name},Identification Number:{threads.ident}")



time.sleep(5)
print(f"{t1.name} is Alive? {t1.is_alive()} " )
print("Nuber of Active Threads",active_count())
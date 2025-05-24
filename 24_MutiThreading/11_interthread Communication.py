""""
thread1 request for event completion to thrrad2. thread2 will give notification thread1 once it's ready.

Ways of implementing.
1. Using Event Object:

event=threading.Event()
event.set() --> Assume Green(True) like event happens so thread can continue
event.clear() --> Assume Red(False) like there is no event happen so thread has to wait untill event occur

isSet() --> return True when event is set
event.wait() --> thread will wait until event is set

2. Using a Condition object:

3. Queue

"""
from threading import *
from time import sleep


def producer():
	sleep(5)
	print("Producer Thread producing Items")
	print("Producer sent event")
	event.set()

def consumer():
	print("Consumer Thread Waiting for Event")
	event.wait()
	print("Consumer Thread got Notification and  consuming Items")

t1=Thread(target=producer,name='ProducerThread')
t2=Thread(target=consumer,name='ConsumerThread')

event=Event()

t1.start()
t2.start()
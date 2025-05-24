"""
By Using Condition Object: 
Event + Lock then it will become condtional object.
- Advanced version of Event Object method as it's always associated with RLock

c=threading.Condition()

c.acquire() --> Thread to acquire lock
c.release() --> Thread release lock internally 
c.wait() --> thread to wait for event notification 
c.wait(time) --> until notification or time expire 
c.notify() -->  To give notification for one waiting thread
c.notifyall()  --> To give notification for all waiting thread 

"""
from threading import *
from time import sleep


def producer():
	c.acquire()
	print("Producer Producing Items.")
	print("Producer Giving Notification.")
	sleep(2)
	c.notify()
	print("Notification Given")
	c.release()

def consumer():
	c.acquire()
	print("Consumer waiting for updation.")
	c.wait(10)
	print("Consumer got Notification and Consuming Message.")
	c.release()

t1=Thread(target=producer)
t2=Thread(target=consumer)
c=Condition()

t1.start()
t2.start()
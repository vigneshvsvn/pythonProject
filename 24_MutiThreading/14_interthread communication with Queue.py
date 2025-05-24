""""
Queue:  has inBuilt Condition  and condition has inbuilt Lock
most powerful inter-thread communication to share data between threads

queue Module contain Queue
import queue
q=queue.Queue()

Methods:
q.put() --> item into the Queue
q.get() --> Remove and return from and item from the Queue

Types of Queue:
1. FIFO: default Queue in python, First in first out
q=queue.Queue()

2. LIFO   : Last in first out
q=queue.LifoQueue()

3. priority Queue: Based on my pritoriy
q=queue.PriorityQueue()

"""

import queue
from random import randint
from threading import Thread
from time import sleep


def producer():
	while True:
		item=randint(1,100)
		print(f"Producer Producing Item {item}")
		q.put(item)
		print('Producer giving notification.')
		sleep(7)

def consumer():
	while True:
		print("Consumer waiting for updation. ")
		print("Consumer consuming the Item",q.get())
		sleep(5)

q=queue.Queue()

t1=Thread(target=producer)
t2=Thread(target=consumer)
t2.start()
t1.start()

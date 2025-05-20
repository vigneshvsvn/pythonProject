"""
Way2: By Extending Thread class means we need to create child class.
		We need to define a job for thread under run() method inside child class

Way3:  Create Thread without extending Thread Class

"""

from threading import *
from time import sleep

#with Extending Class
class MyThread(Thread):
	def run(self):
		for i in range(10):
			print(f'Vignesh {current_thread( ).name} running')
			sleep(1)
#Without extending Thread Class
class Test:
	def display(self):
		for i in range(10):
			print(f'Priya {current_thread( ).name} running')
			sleep(1)
#With Extending
t1=MyThread()  # Main Thread Created Child Thread Object.
t1.start()     # Main Thread started Child Thread

## Without extending class
test_obj=Test()
test_Thread=Thread(target=test_obj.display)
test_Thread.start()
			
for i in range(5) :
	sleep(1)
	print(f'King from {current_thread( ).name}')


import time
from threading import Thread

"""
Assume t1 thread want to wait until t2 thread completes. 
so on t1 thread flow we need to use t2.join()

t2.join(20) --> main thread wait only for 20 secs, once give time exceeds  it will not wait for thread to complete.

"""

def display():
	for i in range(10):
		print("Rama Thread.")
		time.sleep(2)

t=Thread(target=display)
t.start()

t.join(10)       ## wait for Rama thread to complete max of 20 secs
for i in range(10):
	print('Seetha Thread')

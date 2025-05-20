import time
from threading import Thread, current_thread


def doubles(numbers):
	for n in numbers:
		time.sleep(1)
		print(f"{current_thread().name}: The Double of {n} is {2*n}")

def squares(number):
	for n in numbers:
		time.sleep(1)
		print(f"{current_thread().name}: The Square of {n} is {n*n}")
numbers=[1,2,3,4,5,6]
begintime=time.time()

t1=Thread(target=doubles,args=(numbers,))
t2=Thread(target=squares,args=(numbers,))
t1.name='doubles_thread'
t1.start()
t2.name='squares_thread'
t2.start()

t1.join() # Waits until complete of tread 1.
t2.join() # Waits untill complete of thread 2.
endtime=time.time()
print('Total Time taken is ',endtime-begintime)

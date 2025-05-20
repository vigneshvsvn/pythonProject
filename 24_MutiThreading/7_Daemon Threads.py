"""
Daemon: Ghost is not visible in the front
Daemon Thread: Thread which running in the background.
	- Eg: Garbage Collector
	- Main Objective of Daemon Thread is to provide support for non-Daemon Threads

how to check thread is Daemon or not?
current_thread().daemon --> True or False

How make thread to Daemon.
current_thread().daemon=True or False
we need to do it before starting the Thread only.

So the Main Thread is always Non-Daemon as it already started by PVM.


if parent is daemon, then child is also daemon.
if parent is non-Daemon, then child is also non-Daemon.

Note : Once the last Non_daemon terminates automatically, all daemon threads terminate.

"""
import time
from threading import current_thread, Thread


def display():
	time.sleep(5)
	print('Child Thread')



t=Thread(target=display)
print('Parent Thread Is Daemon ?',current_thread().daemon)
print('Child Thread Is Daemon ?',t.daemon)
t.daemon=True
t.start()
print('Child Thread Is Daemon ?',t.daemon)
print('Parent Thread Is Daemon ?',current_thread().daemon)
#t.join()     ## As the main thread completes before Deemon Thread. So the Daemon will also terminate



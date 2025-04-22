import time
import sys


class Test:
	def __init__(self):
		print("Constructor Execution.")
	def __del__(self):
		print("Destructor Execution.")

t1=Test()
t2=t1
t3=t1
print(sys.getrefcount(t1))

del t1
time.sleep(10)
print("Object Not Destroyed after deleting t1")
del t2
time.sleep(10)
print("Object Not Destroyed after deleting t2")
print("Now Removing last reference t3")
del t3
time.sleep(10)
print("End of Program")


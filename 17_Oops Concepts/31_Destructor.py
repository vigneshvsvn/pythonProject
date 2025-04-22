"""
To perform resource deallocation activity GC will call destructor.

GC always call destructor to clean up resources associated with object.
Once Clean up completed GC destroy the Object.


Destructor Syntax: Role of destructor is only to perform clean up. GC is responsible to destroy Object. PVM will take care of it.
__del__()        ## execute before GC destroy Object.
	cleanup activities like dbconnection, network connection .....
"""
import time


class Test:
	def __init__(self):
		print("Initialization Activities ...")
	def __del__(self):
		print("Full filling last wish and Clean up Activities ...")

t=Test()
t=None    ## Test Object reference pointed to None Object. So Test() become no reference then
			# GC will call destructor before destroy Object.
			# Before End of program we are making Object Eligible for GC by making refernce to None Object
time.sleep(10)
t1=Test()
print("End of Program")     ## After END of Program all objects eligible for GC and it will destroy all Objects.
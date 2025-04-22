"""
Garbage collector is to destroy useless Objects. To improve Memory.

When Object become useless and eligible for garbage collector?
	- if object does not contain any reference variable then that object is eligible for Garbage collection.
	- if the reference count is 0 then it's use less.

how to enable and disable GC:
	- By default GC is enabled.

we need to use gc Module



"""
from gc import *
print("GC enabled:",isenabled())  ## To check GC enable or not. By default, GC is enabled
disable()          ## Disable GC using disable() which available in gc module
print("GC enabled:",isenabled())
enable()
print("GC enabled:",isenabled())


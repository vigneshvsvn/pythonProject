"""
Finally, block will not execute only a situation when pvm explicitly shutdown (assume power down).

"""
import os
try:
	print("Try")
	os._exit(0)    ## Explicitly shutting down PVM. Power down scenario. Finally, won't be executed
	
except ValueError as msg:
	print("Except")
finally:
	print("Finally Block.")
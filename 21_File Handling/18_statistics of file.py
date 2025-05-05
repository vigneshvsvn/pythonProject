"""

"""
import os
from datetime import *


statistics=os.stat('abc.txt')
print(statistics)
print("Last Modified time:",datetime.fromtimestamp(statistics.st_mtime) )
print("Size of File:",statistics.st_size)


# for k,v in list(statistics):
#  	print(f"Key {k}",v)

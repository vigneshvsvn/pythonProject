"""
If we want to perform any action like read,Write… First, we need to open files.

syn tax=open()
1. filename
2. Modes for Text files.if we suffix with b then it will become binary. 
	r--> for read and default,
	w--> for write Operation, if already available old data will be overwritten. If a specified file is not available, it will create.
	a --> append, If any data is available in an existing file, then it will append. If a file is not available, then it will create it.
	r+ --> read & write. during Write existing data will overwrite. If a file is not there, then File not Found error will appear.
	w+,--> Write and Read. By default, it will overwrite existing data.  If a specified file already not available, then it will create.
	a+, --> append and read. Existing data will not overwrite. File will create if not already  available.
	x --> Exclusive.Meant for write operation. If a file is already available, then we get a file exists error.

"""


try:
	f=open('abc.txt','r')
	
except FileNotFoundError as msg:
	print("Exception Name:",msg.__class__.__name__)
	print("Exception Description:",msg)
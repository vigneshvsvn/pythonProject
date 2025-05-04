"""
tell() --> It will give the current position or Index of cursor.  The First position or index is 0
seek() --> To Move the cursor to a particular position
	f.seek(offset,fromwhere)
		Offset --> Howmany Chars need to move
		fromwhere:
		0 --> From Begin of file
		1 --> From Current Position
		2 -->  From End of FIle
"""
## tell()
f=open('abc.txt','r')
print("Current Position",f.tell())
print(f.read(2))
print("Current Position",f.tell())
print(f.read(2))
print("Current Position",f.tell())
print(f.read(1))
print("Current Position",f.tell())
print(f.read(1))
print("Current Position",f.tell())

## seek()
f.seek(10)
print("Current Position",f.tell())




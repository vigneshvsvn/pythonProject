"""
if we want to handle binary data then we need to go for byes and bytearray (images, videos,audio  .....)
Bytes can't be assigned   or modified      (Immutable)
bytes --> can be used from 0-255 only
	  --> indexing and slicing allowed as it's ordered
	  --> can't be assigned or modified

Bytearray can be assigned or Modified       (mutable)
  	--> if we want mutable bytes then we need to for bytearray
"""

lst=[20,30,40,234]
print(type(lst))
print(lst)



print(4*'#'+"Bytes")
b=bytes(lst)             ## Need to call inbuilt function to create byes type
print(type(b))
for i in b:
	print(i)


print(4*'#'+"Byte Array")
b1=bytearray(lst)
b1[2]=10
for i in b1:
	print(i)

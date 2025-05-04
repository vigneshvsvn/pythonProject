"""
f=open('abc.txt','r')
1. f.read() --> Total data will be returned as string.
2. f.read(n) --> To read n chars from the File.
3. f.readline() --> first line will return and when we call second time second line will return
4. f.readlines() --> Read all lines and return as List.

"""

f=open('abc.txt','r')
# fulldata=f.read()
# print(fulldata)

nChars=f.read(10)
print(nChars)


f.close()

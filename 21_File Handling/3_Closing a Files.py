""""
After required operation on files. We need to close the files, and it's highly recommended.
Advantage:
- If we close, all systems, resources will be released. And Increase the Performances.

Syntax:
f=open(ábc.txt,'a')    -- Read is the default Mode.
# required Operations from opened files
f.close()

Properties of File Object:



"""
f=open('abc.txt','x')
print("Name of File",f.name)
print("Mode of File:",f.mode)
print("File Closed:",f.closed)
print('Readable:',f.readable())
print("Writable:",f.writable())
f.close()
print("File Closed:",f.closed)
f.








"""

"""
## 1. Read Line
# f=open('abc.txt','r')
# line1=f.readline()
# print('First Line:',line1,end='')
# line2=f.readline()
# print("Second Line:",line2,end='')
# f.close()

##2. Read Lines to list
f=open('abc.txt','r')
list=f.readlines()
print(list)

for each_line in list:
	print(each_line,end='')
f.close()
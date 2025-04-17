str="Learning Python is very Easy"
print(str)
lst=str.split()
lst2=[]
for content in lst:
	   lst2.append(content[::-1])
#print(lst2)
print(" ".join(lst2))


from operator import index

str="Learning Python is very Easy"
print(str)
lst=str.split()
lst2=[]
i=0
while i<len(lst):
	if i%2==0:
		lst2.append(lst[i])
	else:
		lst2.append(lst[i][::-1])
	i+=1
print(" ".join(lst2))


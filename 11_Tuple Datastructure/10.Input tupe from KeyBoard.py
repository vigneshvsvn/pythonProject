t=eval(input("Enter Tuple:"))
print(t)
s=0

for x in t:
	s=s+x

print("Sum of given tuple is",s)
average=s/len(t)

print("Average for given tuple is",average)


####using inbuilt functions
s=sum(t)
print("Sum Using inbuilt function:",s)

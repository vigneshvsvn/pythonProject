n=int(input("Enter Number of Students"))
d={}
for i in range(n):
	name=input("Enter Name of Student:")
	marks=input("Enter Marks of Student:")
	d[name]=marks

print(d)

for each_name in d:
	print(each_name,'\t\t',d[each_name])


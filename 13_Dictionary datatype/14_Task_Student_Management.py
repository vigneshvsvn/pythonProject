from re import search

numberOfStudents=int(input("Enter Total Number of Students:"))
d={}
for each in range(1,numberOfStudents+1):
	name=input(f"Enter Name of Student {each}:")
	marks=int(input(f"Enter Mark of Student {each}:"))
	d[name]=marks



# for k,v in d.items():
# 	print(k,'\t\t',v)

while True:
	searchname=input("Enter Student name to get marks: ")
	marks=d.get(searchname,-1)

	if marks==-1:
		print(f"No Student found with name {searchname}.")
	else:
		print('*' * 30)
		print("Name \t\t Marks ")
		print('*' * 30)
		print(searchname,'\t',marks)

	nextstudent=input("Do you want to search for another stuudent Mark (Yes or No)? ")
	if nextstudent.lower() == 'Yes'.lower():
		continue
	else:
		break

print("Search Completed. Thanks you for Using Student App.... ")
	

	
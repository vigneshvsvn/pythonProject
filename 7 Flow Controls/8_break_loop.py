"""
Break will break only Enclosing Loop not entire program.

In Nested Loop we are using break in inner loop. Then it will break only inner loop. Outer loop will continue.

"""

lst=[3,6,9,5,12]
for i in lst:
	if i==5:
		break
	print(i)
print("End")
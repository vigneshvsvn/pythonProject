"""
List inside nested list.
"""
l=[10,20,[30,40]]               ## this is call nested list.
print(l[0])
print(l[1])
print(l[2])
print(l[2][0])      ## how to access nested list
print(l[2][1])

matrix_list=[[10,20,30],[40,50,60],[70,80,90]]
print(matrix_list)
for each_element in matrix_list:
	#print(each_element)
	for y in each_element:
		print(y,end=' ')
	print()

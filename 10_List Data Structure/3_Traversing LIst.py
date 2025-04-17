"""


"""


lst=[0,1,2,3,4,5,6,7,8,9,10]

## By using While Loop
i=0
while i < len(lst):
	print(f"Element in Index {i} is {lst[i]}")
	i=i+1


## By Using For loop --> this is the best choice for accessing sequence.
for each_value in lst:
	print(each_value)

for each_value in lst[0::2]:     ## To take only Even Indexes 
	print(each_value)

###
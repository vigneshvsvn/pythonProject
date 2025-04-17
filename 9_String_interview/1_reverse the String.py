name='vignesh'
#####Way 1   using slice Operator.
print(name[-1::-1])
print(name[::-1])  ## For -ve step if start not given then default start  will be -1

## Way 2 using reversed function
# s2=reversed(name)
# print(type(s2))
# for x in s2:
# 	print(x)
# output=''.join(s2)
# print(output)

## Using While Loop
length=len(name)
output=''
while length > 0:
	output=output+name[length-1]
	length=length-1
print(output)
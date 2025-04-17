"""
1. By using Index
2. By Using Slice Operator
	lst[begin:end:step]
	If Step Value
	+Ve --> Move Forward direction , begin to end-1   , Default start will be 0th Index, If End value 0 then list will be always Empty
	-Ve --> Move Backward direction, begin to end+1   , Default start will be -1 Index , if end value -1 then list will be always Empty

"""
lst=[10,20,30,40,50,60,70,80,90,100]

## Access using Index
print(lst[0],lst[-4])
print(lst[-1])
#print(lst[100])   ## Index out of error

## Access using Slice Operator. Same as like String.
print(lst[2:7])
print(lst[2:7:2])
print(lst[4::2])
print(lst[8:2:-2])
print(lst[4:100])
print(lst[4:0:2])
print(lst[::1])
print(lst[::-1])



from itertools import count

input='aaaabbbccz'
"""
ouput expected= 'a4b3c2z1'
"""
count=1
prev_char=input[0]
output=''
i=1

while i < len(input):
	if input[i]==prev_char:
		count=count+1
	else:
		output=output+str(count)+prev_char
		prev_char=input[i]
		count=1
	i=i+1

print(output)

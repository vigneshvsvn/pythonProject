input='a4z3c2'
"""
output expected: 'aaaabbbcc'
"""
output=''

for each_char in input:
	if each_char.isalpha()==True:
		x=each_char
	else:
		output=output + x*int(each_char)

print(input)
print(output)
print(''.join(sorted(output)))     ## If we want sorted order.
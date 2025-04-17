input='asdfasdf'
"""
Expected output='asdf'
"""
#### Way 1
output=''
for each in input:
	if each not in output:
		output=output+each
	else:
		pass
print(output)

#### Using List Way 2
lst=[]
for each in input:
	if each not in lst:
		lst.append(each)
print(''.join(lst))

## using Set
s=set(input)
print(''.join(sorted(s)))
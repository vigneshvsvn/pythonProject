input='a4k3b2'
"""
expected output aeknbd

ord('a') -->    97
chr(97) --> a
"""

print(input)
output=''
for each in input:
	if each.isalpha()==True:
		prev=each
		output=output+each
	else:
        ##output=output+
		output=output + chr(ord(prev)+int(each))
		pass
print(output)
from os import lstat

s1='Ravi'
s2='Tejas'
"""
Output Expected: RTaevjia
"""
i,j=0,0
output=''

while  i < len(s1) or j < len(s2):
	if  i < len(s1) :
		output = output + s1[i]
		i = i + 1
	if  j < len(s2):
		output = output + s2[j]
		j=j+1
print(output)

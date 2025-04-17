"""
To Find number of occurrence of give  string.
str.count(str[,start[,end])
"""
s='abbasdgbasdebdsb'
print(s.count('b'))
print(s.count('bb'))
print(s.count('z'))        ## if not found it will retrun 0

print(s.count('b',3,100))
s='BBBB'
print(s.count("B"))
print(s.count("BB"))

### To Find Index of all occurrences of given substring.

str='ABCABCABCA'
substr='BC'
i=str.find(substr)
if i==-1:
	print("Substring Not Found")
else:
	while i != -1:
		print(f"{substr} present at index {i}.")
		i=str.find(substr,i+len(substr))
	print(f"{substr} occurrence {str.count(substr)} times.")



import re
pattern="\d"
#pattern='a7b@k9 zA.aacaaaa'
str='a7b@k9 zA.aacaaaa'
list=re.findall(pattern,str)
print(list)
for each in list:
	print(each)
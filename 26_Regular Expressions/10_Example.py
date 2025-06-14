"""
Mobile Number extract from File.


"""

import re

f1=open('input.txt','r')
f2=open('Mobilenumber.txt','w')
pattern='([6-9][0-9]{9})|(0[6-9][0-9]{9})|(91[6-9][0-9]{9})|([+]91[6-9][0-9]{9})'
for line in f1:
	list=re.findall(pattern,line)
	#print(list)
	for n in list:
		f2.write(n[0]+'\n')
f1.close()
f2.close()
print("Extraction Completed.")
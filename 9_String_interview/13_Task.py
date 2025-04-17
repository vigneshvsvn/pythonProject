s='asdfdfsd'
d={}
for each in s:
	d[each]=d.get(each,0)+1

output=''
for k,v in d.items():
	output=output+str(v)+k
print(output)

output=''
for k,v in d.items():
	output=output+k+str(v)
print(output)

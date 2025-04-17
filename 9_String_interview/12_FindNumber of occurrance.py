s='asdfdfsd'
s_unqiue=''.join(sorted(set(s)))
print(s_unqiue)
for each in s_unqiue:
	print(f"{each} present {s.count(each)} in given String")

####### Without using Count Method
d={}
for each in s:
	d[each]=d.get(each,0)+1

print(d)
for k,v in d.items():
	print(k,v)

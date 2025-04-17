word=str(input("Enter the Input word:"))

d={}

for each_char in word:
	d[each_char]=d.get(each_char,0)+1

print(d)


for k,v in d.items():
	print(f"Char {k} occurs {v} times in the Word")
word=str(input("Enter the Input word:"))

vowels={'a','e','i','o','u'}
d={}
for each in word:
	if each in vowels:
		d[each]=d.get(each,0)+1

print(d)

for k,v in d.items():
	print(f"Char {k} occurs {v} times in the Word")
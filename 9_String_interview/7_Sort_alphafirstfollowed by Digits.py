s="B4A1D3"
"""
Expected Ouptput: ABD13
"""
print(sorted(s))
alpha=[]
digits=[]
for each_char in s:
	if each_char.isdigit()==True:
		digits.append(each_char)
	elif each_char.isalpha()==True:
		alpha.append(each_char)
	else:
		pass
print(alpha)
print(digits)
print(''.join(sorted(alpha)+sorted(digits)))
d1={100:'A',200:'B',300:'C',400:'D'}
getKey=int(input('Enter Key:'))
print(f"Values for Given Key {getKey}:",d1.get(getKey,"Given Key unavailable in the Dictionary"))

getValue=input('Enter Key:')
for key,val in d1.items():
	if val==getValue:
		print(key)


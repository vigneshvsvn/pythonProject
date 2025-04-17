
## 1st Example
l1=[(10,20,30),(40,50,60)]             ## List of Tuples
print(l1)
print(l1[0])
print(l1[0][1])
print(l1[-1][-1])

## 2nd Exmple
d={
	'cars':('Nexa','Brezza','Innova'),
	'mobiles':('apple','samsung','vivo')
}
print(d)
print(d['cars'])
print(d['cars'][2])
print(d.get('cars')[2])
print(d.get('mobiles'))
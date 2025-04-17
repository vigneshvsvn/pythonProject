"""
 d.keys()
d.values()
d.items()
 
"""
d1={100:'A',200:'B',300:'C',400:'D'}
keys=d1.keys()
print(keys)       ##dict_keys([100, 200, 300, 400])
for each_key in keys:
	print(each_key)

values=d1.values()
print(values)        # dict_values(['A', 'B', 'C', 'D'])
for each_values in values:
	print(each_values)

items=d1.items()
print(items)      # dict_items([(100, 'A'), (200, 'B'), (300, 'C'), (400, 'D')])

for key1,value1 in items:
	print(key1,value1)

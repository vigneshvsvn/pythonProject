shops={
	'store1': {
		       'name':'Ayyanar Stores',
				'items':[
						 {'name':'soap','quantity':20},
						 {'name':'brush','quantity':30},
						 {'name':'pen','quantity':50}
						 ]
				},
	'store2': {
		       'name':'Prince Hotel',
				'items':[
					     {'name':'Parota','quantity':200},
						 {'name':'ChickenChops','quantity':50},
						 {'name':'Tandoori_Chicken','quantity':25}
						 ]
				}
}
print(shops)
print(shops['store1']['name'])          ## Approach 1
print(shops.get('store2').get('name'))  ## Approach 2
print('*'*30)
                                                                                   	

print("Items available on Store 2 are as below.")
for each_item in shops.get('store2').get('items'):
	print(each_item['name'],':',each_item['quantity'])
print('*'*30)

for each_item in shops.get('store2').get('items') :
	if each_item['name']=='ChickenChops':
		print("Quantity of Chicken Chops:",each_item['quantity'])
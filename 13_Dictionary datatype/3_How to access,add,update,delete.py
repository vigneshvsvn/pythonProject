"""
 1 Accessing value using Key. d[key]
 2. add/update new key value pair
 	d[key]=value
 	If key is already available then update existing value, else create new entry of key value pairs
3. how to delete data from dict
	- using del d[700],d[100]


"""
d={100:'Vignesh',200:"Priya",300:'Privika'}
print(d,"Length:",len(d))
print(d[100])
if 700 in d.keys():
	print(d[700])     #KeyError: 700  as key 700 not present  . So need to check present or not
d[700]="New baby"      ##
print(d)
del d[700]          ## delete key matches 700
print(d)
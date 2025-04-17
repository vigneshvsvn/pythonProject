"""
*  Group or objects as Key value pairs.
	Eg: {RollNumber : Name }
*  Syntax: {key1: value1, key2: value2 .....}
* Duplicate Keys are not allowed
* Duplicate values are allowed.
* Insertion order not preserved and it's based on Key hashcode
* Index, slicing are not allowed as it's not having any Ordering
* For both Key and values heterogeneous objects allowed
* It's mutable
* Dynamic in nature. As it's Growable
* if we are tying to add duplicate key then it will update with new value.


"""

d={100:'Vignesh',200:"Priya",300:'Privika'}
print(d)
d[300]="Kutty Naye"    # 
print(d)

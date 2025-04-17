"""
- Set will not allow duplicate, If we add set will omit duplicates  not throw an error.
- Un Ordered list 
- Set uses flower bracket   {}
- HETEROGENEOUS -- Different data types are allowed
- Set is Growable and Mutable.
- Does not follow order  , So Indexing , slicing and repeataions not allowed
	append vs add
	- in list we used append() as it will be at the last, to maintain order
	- add() used in set as there no order.
- s={} will consider as dict type not set.
- To create empty set we need to you set() eg: s=set()
"""
s={1,3,5,3,"vignesh"}
s1={1,2,3}
s2={2,1,3}
s3={3,2,1}
s_emptyset=set()          ### To create empty set
print(s)     ### second time 3 will be ignored as set will not allow duplicate but order can't be same.
print(s_emptyset)
### s1,s2,s3 are equal as set is unordered 
print(s1)
print(s2)
print(s3)
s.add(20)
s.update([88,99])          ## Does not give any order
print(s)
s.remove(99)
print(s)

########## Frozen Set

"""
- same as set but it's immutable(can't be changed).
- need to use frozenset() function to create frozen set.


"""

fs=frozenset(s)
print(type(fs),fs)
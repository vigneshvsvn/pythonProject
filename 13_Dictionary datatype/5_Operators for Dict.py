"""
+ and - not allowed
* not applicable    as duplicate keys not allowed.

equality : == and != --> Allowed.Order will be ignored while comparing

Relational : <,>,<=,>= are not allowed in Dict.

Membership : in and not in are allowed. It will check only for Keys not on Values.
"""
d1={100:'A',200:'B'}
d2={300:'C',400:'D'}
d3={200:'B',100:'A'}
print(d1==d2)
print(d1==d3)   ## ignore order and compare key values. So True
print(100 in d1)
print(300 in d1)
print('A' in d1)   ## A is not available in d1 as Key. So Value will not consider 

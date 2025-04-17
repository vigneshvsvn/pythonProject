"""
d1.setdefault(k,v) --> if key is not available then  add key and Value  to dict.
						if Key already exists then rerun existing value and does not modify anything

"""
d1={100:'A',200:'B',300:'C',400:'D'}

d1.setdefault(500,'E')            ##  key 500 is already not available, so it will be added    to dict
print(d1)
print(d1.setdefault(100,"F"))     ##    rerun  value 'A' as 100 is existing Key so it's existing value will be returned.
print(d1)
d1={100:'A',200:'B',300:'C',400:'D'}
d2=d1               ## Aliasing 
print(id(d1),id(d2))
print(d1,d2)
d3=d1.copy()
print(id(d3),d3)

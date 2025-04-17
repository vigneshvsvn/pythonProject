"""
1.union()  --> All elements in the s1 and s2.  we can use '|' as alternative.
2. intersection() --> Common elements in s1 and s2. We can use '&' as alternative.
3. difference() method  --> element present in s1 and not in s2. Means element should be only in s1 not is s2. We can use '-' minus
4. symmetric_difference() --> Elemet present only in s1 and s2 means  Except common between s1 and s2. For symbolic represendtion we can use cap '^'
"""

s1={10,20,30,40}
s2={30,40,50,60,70}
print("s1:",s1)
print("s2:",s2)
s3=s1.union(s2)
print("s3:",s3)
s4=s1|s2            ## We can use union() or by   '|'  or operator. Will give same result.
print("s4:",s4)
s5=s1.intersection(s2)
print("s5:",s5)
s6=s1&s2           ## intersection() or symbolic representation  '&' it will give same resoutls
print("s6",s6)
s7=s1.difference(s2)
print("s7:",s7)
s8=s1-s2            ## We can use minus operator to do same operation of different()
print("s8:",s8)
s9=s1.symmetric_difference(s2)
print("s9:",s9)
s10=s1^s2        ## ^ is the symbolic representation of symmetric_difference()
print("s10:",s10 )


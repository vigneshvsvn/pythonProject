"""
class specific reverse method  is not available as tuple immutable.
But we can create new tuple by using python inbuilt function using reversed().


"""
t=(10,20,30,10,30,20,10,45)
print(t)
t1=tuple(reversed(t))
print(t1)
t2=tuple(sorted(t))
t3=tuple(sorted(t,reverse=True))
print(t2,t3)

print("Max of t1:",max(t1))
print("Min of t1:",min(t1))

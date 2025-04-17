"""
+ Concat operator  --> Create new tuple, existing tuple can't modify. Both operand should be tuple only.
* repetition     --> One should be int other should be tuple
"""
t1=(10,20,30,)
t2=(40,50,60)
t3=t1+t2       # Concatenation
print(t1,t2)
print(t3)
t4=t1*2       # repetition
print(t4)
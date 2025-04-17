"""
Arithmetic Operators: + and * operator can't be used.
Equality operators ==,!= is possible
Relations Operator : Not meaning fully implemented in python. Even thought it's in use not suggested to use. As order is not there it's not proper.
membership operators: in and not in operator.

"""
s1={10,20,30}
s2={30,40,50}
##s3=s1+s2     ##  TypeError: unsupported operand type(s) for +: 'set' and 'set'    we can't use   + operator
#s3=s1*3        ## TypeError: unsupported operand type(s) for *: 'set' and 'int'     we can't use   * operator
print(s1==s2)       ## False as elements are not equal
s3={30,10,20}
print(s1==s3)       ## all elements should be same irrespective of Order . So it's True

print(s1<s2)      ## Applicable for set but it's not proper. Not to use in python

print( "50 in s2", 50 in s2)
print( "50 not in s2", 50 not in s2)
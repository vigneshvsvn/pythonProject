"""
+ --> Meant for concat. Both arguments should be string.
* --> repetition. One argument should be int and other should be string.

Membership:
in
not in

<,<=,>,>= It works but based on Unicode value.
==, !=
"""
from itertools import product

s="Vignesh"

print('V' in s)
print('Vig' in s)
print('z' in s)

print(s *3)        # repetition
print("Hello " + s)

print(ord('a'))    ## Convert to unicode
print(chr(97))     ## convert unicode to alpha




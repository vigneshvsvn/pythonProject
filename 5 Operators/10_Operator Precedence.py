""""
In which order operator to execute is decided by operator precedence.

if both operator same priority then left will take first 

1.  () --> parenthesis
2. **
3. ~,- (bit wise complement),(unary minus )
4. *,/,%,??
5. +, -
6. << , >>
7. & bit wise and
8. ^
9. |
10. >,>=,<,<=,==,!=
11.is, is not  ( identity operator)
12. in, not in ( membership operator)
13.  not
14. and
15. or
"""

print(10+2*3)
print((10+2)*3)
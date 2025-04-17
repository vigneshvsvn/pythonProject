""""
if operator applicaple for 2 operand/ agrument call binary Operator Eg: (A+B)
If operator applicable for 3 operands/arguments call Ternary Operator
syntax:
c= (first value) if (condition)  else (second Value)
"""
a=56
b=20
c=45
d=30 if a>b else 40
print(d)

###Nesting of Ternary Operation
min= a if a<b and a<c else b if b<c else c
print(min)
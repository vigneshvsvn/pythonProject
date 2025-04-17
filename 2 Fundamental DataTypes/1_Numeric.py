#Integer.......    Whole number without any decimal  point
## To represent to long integral  we had long type but only in python 2. So no more long after 3.x
"""
Integer can represent in 4 forms in python
decimal Form (base 10)   --> Default form  (0-9)
binary form (base 2)      --> allowed digits (0,1)    --> prefixed with 0b or 0B
Octal Form (base 8)       --> allowed digit (0-7)     --> prefixed with 0o or 0O     eg: 0o123 --> 
Hexa form (base 16)        --> allowed digit (0-9 and a-f or A-F) --> prefixed with    0x or 0X
"""
a=13
b=100
c=13
d= 0B1111         ## Binary representation
e=0o123           ## Octal representation
f=0xaf            ## Hexa Decimal Representations
print("Decimal:",a,b,c)
print ("Binary d:",d)
print("Octal:",e)
print("Hexa:",f)
print(type (a),type(b),type(c))    #### type() used to find data type of identifier or variable
print(id (a),id(b),id(c))          #### id() used to find address of the variable

"""
How to convert one base to other using base conversion functions.      It only available for Integer type
bin()      --> Other base to Binary 
oct()      --> other base to Octal 
hex()      -->  other base to hexa decimal
"""
### To Binary 
print("Binary form of 10 is ", bin(10))
print("Binary form of 0o123 is ", bin(0o123))
print("Binary for of 0xff is",bin(0xff))

#Floating.......
"""
to use decimal places we need to use floating point values.
bin,oct and hex forms not allowed in float type.
exponential form or scientific notation allowed  only for floating point (1.23e3)

"""


x=12.0
y=-9.98
z=205.1
u=1.23e3
print(x,y,z,u)
print(type(x), type(x),type(z),type(u))

## 

"""     Evaluate the expression and return boolean (True or false)
		Relational Operator
		Comparesion based on unicode or ascii value 
==
!=
>
<
<=
>=
"""
x,y=77,78
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x<=y)
print(x>=y)

#############String Comparision  
s1='a'
s2='b'
print(ord('a'),ord('b'))   ## ordinal Value: To Find Unicode Value for given Char. We need to use ord()
print(chr(97))    ## To convert unicode value to chara we need to chr()
print(s1>s2)          ## comparision will happen based on Unicode value

#### Boolean  Comparision    True  =1 and False =0
print(True > False)

### Chaining of Relational  Operator
print(10<20<30<40)           ## All comp should true: 10 <20 , 20<30 and 30<40 all are True
print(10<20<30<40>50)        ##


print(10==10.0)

#### diff between == vs is()
# == for value or content comparision
# is() (reference or address comparision)
print("== Vs is Operator with List sample ")
l1=[10,20,30]
l2=[10,20,30]
l3=l2
print(l1,id(l1))
print(l2,id(l2))
print(l3,id(l3))
print(l1==l2)
print(l1 is l2 )

print(l3==l2)
print(l3 is l2 )
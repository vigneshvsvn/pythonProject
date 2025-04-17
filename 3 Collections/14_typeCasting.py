"""
Type casting or type coersion. We have 5 pythion function do it.
1.int()   --> To Convert from other types to int. int("5") string value should only integer with base 10 , int(5.98), int(10=20j) --> complex can't convert to int
2.float() -->    float(int value) int value can be any form (base10 , binary, hex, octal)  , Sting to float only value allowed int or float with base10 form.
3.complex()
4.bool()
5.str()
"""
f=10.3
c=10+5j
b=True
s1="vignesh"
s2="5"
i=99

###### 1. int()
print(3*"#"+ "int()" + 3*"#")
print(int(10.3))
print(int(b))
print(int(s2))  ## S2 can't be converted as value is not integer number.
## print(int(c))    ## Complex to int is not allowed we will get type error

####### 2.float ()
print(3*"#"+ "float()" + 3*"#")
print(float(i))
## print(float(c)) Complex to flot is not allowed
print(float(b))
print(float(s2))
print(float("20.76"))
## print(float(s1))           Value of s1 is not in int or float with base10

########## 3. complex()
print(3*"#"+ "complex()" + 3*"#")
print(complex(s2))         ## if we pass only one argument it will consider only real part and imaginary part become 0j
print(complex(f))
print(complex(b))

## with two argument to cast both real and imaginary part complex(x,y) x: real part and y:imaginary part
print(complex(10,45))
#print(complex("10","20"))          ## if you want to pass  both part as string not allowed. Also second argument 

########## 4. bool()
print(3*"#"+ "bool()" + 3*"#")
print(bool(i))
print(bool(0.0))        
print(bool("False"))    ## print True
print(bool(0+0j))      ## Both real and ima part zero then False else it will true
print(bool(0+1j))
print(bool(''))     ## empty string consider as False else True

########## 5. str()
print(3*"#"+ "bool()" + 3*"#")
print(str(10))
print(str(10.5))
print(str(0+5j))
print(str(True))


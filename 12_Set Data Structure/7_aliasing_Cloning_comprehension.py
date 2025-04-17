

s1={10,20,30,40,50,1,2,3,4}
s2=s1  ## Aliasing by creating duplicate reference variable of same object. Change in any one will impact other. s1 changes will impact s2. s2 change will impact s1
s3=s1.copy()  ## Cloning, by creating new object with new reference.  If we perform any changes on s3 it will not impact on s1.

print(id(s1),id(s2),id(s3))

print(s1,s2,s3)
s1.pop()    ## it will impact s1
s3.pop()    ## it will not impact s2. Changes will happen only for s3
s3.pop()
print(s1,s2,s3)

s4={ i*i for i in range(1,6)}          ## create Square of fist five numbers.
print(s4)
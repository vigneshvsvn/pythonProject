"""
+
-
*
/    --> always return floating point
%
**   --> Exponent operator   2**3 means (2 power 3)
//   --> Integer Division operator called floor division no decimal number .
	--> if both arguments are int then results will be integer. If any one is float then result will be float type
"""
print(1+3)
print(6-3)
print(2*3)
print(2/3)
print(2%3)
print(2**3)
print(2.0//3)

## (+) For String
print('10'+'20')      ## between two string if we apply + then it do concat    Note: Both should be string else it will through a type error.
print('10'+str(20))    ## need to type cast to str type.

## (*) for String      ## one argument should be string and other should be int type. Call Repeatation 

print("Vignesh"*3)
print("Vignesh"*False)           ## Empty String 
print("Vignesh"*True)


### Anything Division by zero  : always ZeroDivision error
##print(10/0)

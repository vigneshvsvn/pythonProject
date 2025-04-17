"""
single or Double Quote --> consider as String
Triple quote --> 1. Multiple line string letters 2. Documentation String 

- In python there is no char datatype. So even single char also consider as String type only.

Accessing:
1. By using Index
	- Positive   (Left to Right ) Eg: "Vignesh" 0--> v ; 1--> i ; 2--> g ; 3 --> n ;4  --> e ;5 --> s; 6 --> h
	- Negative Index (Right to Left) Eg: "Vignesh"    -1 --> h; -2-->s ; -3 --> e ; -4 --> n ; -5 --> g ; -6 --> i ; -7 --> v
	- If we are tying to access more than available Index then we will get Index out of Bound error.
2. Slice Operator 

"""

name="Vignesh"
welcome="""Welcome 
to 
Python Course.
"""
##s='This is ' symbol'   In valid
s="This is ' symbol"  ## Valid  as
s='This is \' symbol' ## Valide as we escape ' special meaning by using \
s="""This is ' symbol"""    # this is the easy way if string contains special meaning symbols in the string.

### To print char in positive Index and Negative Index
i=0
for x in name:
	print(f"Character present at Positive Index {i} and Negative Index {i-len(name)}  is {x}")
	i+=1

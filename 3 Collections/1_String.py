"""
Any sequence for Characters is called String.
' and " can be used to represent the String.
Triple Quote can be used for Multiple line string and also to use ' and "" as normal char in string.

there is no char data type in python.

"""


s="vignesh"         ### Single line
print(s)
s="Vignesh is Learning 'Python'"       ### To use single ' to print in the string then use double " to represent string.
print(s)
s='vignesh is Learning "Python"'                                   ### To use " as normal char in sting
print(s)

## To use ' and " as normal character in string then also we can use """
s="""'Vignesh' is Learning "Python" """
print(s)

### To Print multiple line String we need to use triple Quotes
s1="""Your are 
the 
Destiny"""
print(s1)

#------------------------------        To GO to particular line
print(s[0])


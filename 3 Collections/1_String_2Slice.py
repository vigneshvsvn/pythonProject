"""
Slicing --> getting part of the string by using slice operator.
Syntax: s[begin Index: End-1 Index: Step Value]
s[3:9] --> from 3rd index upto 9-1= 8th Index
"""

s="vigneshkumar"

### Slicing             Means start from 0 index with 5 chars  means [0,1,2,3,4,5]             syntax[start index:end index: step value]
print(s[0:5])
print(s[0:])            ## If we are not giving end, then Start from given index (here it is 0 index) and print rest all index
print(s[:8])            ## print from begin to 8-1= 7th Index
print(s[:])             ## Entire String will be considered as slice output
print(s[1:100])         ## To Index out of range in slice. It will consider up to max index only
print(s[4:1])           ## Return Empty String as there is no index 1 after 4th (Start), empty string will get
## convert first char of string to Capital
print("Starting letter to upper case:",s[0].upper()+s[1:])
## convert Last char of string to Capital
print("Ending letter to upper case:",s[0:len(s)-1]+s[-1].upper())
## Convert first and last char to capital
print("First and last char converted to Capital:",s[0].upper()+s[1:len(s)-1]+s[-1].upper())



print(s[-3:-1])
print(s[0:15:2])        ##       step by two chars
print(s[15::-1])        ##        Print in reverse  as we know string s is having length of 15
print(s[::-1])           ##Print in Reverse


############### Strip function used to remove the space and begin and end of the string
print(s.strip())
print(s.lstrip())


############# To Find the index of a patten
print(s.find("a",0,len(s)))    ### If not found then return -1        otherwise return first occurrence Index
print(s.count("a"))            ### Two Occurs
print(s.replace("awesome","Super"))
print(s)

#################Cases
print(s.upper())
print(s.lower())
print(s.title())

#########
########## Repetations

print(s[2]*3)

####To Check Length
print(len(s))


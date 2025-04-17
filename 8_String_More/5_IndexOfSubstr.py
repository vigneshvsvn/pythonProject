"""
To find index of String
1. find(str,start index,end index)   --> Left to right until matched. return index of first occurrence   . Incase not found then return -1
2. rfind()    --> right to left
3. index()  -->     same like find but if value not available then return Value Error. Where as in find() we will get -1
4. rindex()
"""
s="ABCDEFGHIJBA"
print(s.find('B'))         # 1 --> Index of First Occurrence from left to right
print(s.find('Z'))         # -1 --> If not available then return -1
print(s.rfind('B'))        # 3 -->
print(s.find('A',3,20))
print(s.rfind('B'))

#print(s.index('Z'))        ## Not available in given String then we will get value error.

mail="vigneshvsvn@gmail.com"

print(mail.find("@"))
print(mail.find("@gmail"))
userid=mail[0:mail.find("@")]
print(userid)



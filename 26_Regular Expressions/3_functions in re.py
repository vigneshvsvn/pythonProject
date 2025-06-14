"""


1.match() --> To check give pattern start with on String or not. If match found it return match object otherwise retuning None
2.fullmatch() --> To check total target string matched with given pattern or not. Complete match
3.search()-->  We can use search given pattern in serach object.
4.findall()  --> all occurance of the match -- retrun list object
5.finditer(): re.finditer(pattern,str) --> rerun match iterator
6.sub()  --> substitute  or replacement
7.subn()  --> substitute or replacement but return as tuple. (str,int) --> replaced string and replacement count
8.split() --> to split target string according to pattern.
9.compile()


"""


import re
pattern='aa{1}7'
#pattern='a7b@k9 zA.aacaaaa'
str='a7b@k9 zA.aacaaaa'
mobile_pattern='[6-9]\d{9}'
mobile_number='4587421965'
#matcher=re.match(pattern,str)
matcher=re.fullmatch(mobile_pattern,mobile_number)
if matcher is not None:
	print(f"Target string start with {matcher.group()}")
else:
	print(f'target string not start with {pattern}')
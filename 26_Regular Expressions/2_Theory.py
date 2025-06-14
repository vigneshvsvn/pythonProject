"""
1. character class:
we can use char classes to match group of characters.
	Eg:
	[abc] --> a or b or c
	[^abc]  --> except a or b or c.
	[a-z], [b-m] --> any lower case symbol , a to Z , b to m like this
	[A-Z] --> any upper case symbol
	[a-zA-Z] --> any lower and upper case
	[0-9] --> any digit between 0 and 9
	[0-9a-zA-Z] --> any alpba numeric char
	[^0-9a-zA-Z]  --> Except alpha Numeric chars

2. Predefined char class:
	'\d' --> any digits means [0-9]
	'\D' --> other than digits means [^0-9]
	'\w' --> any alphanumeric character means [a-zA-Z0-9]
	'\W' --> any char except alphanumeric char means [^a-zA-Z0-9]
	'\s' --> space char
	'\S' --> except space Char
	'.'  --> Any char including special char

3. Quantifiers:
we can use quantifier to specify the number of Occurrences to match.
Eg:
'a' --> exactly one 'a'
'a+' --> At least one or more match   but not space
'a*' --> Any number of 'a' including zero number
'a?' --> Almost one 'a'
{n} --> a{2) means 'aa' exactly n times
{n,} --> a{2,} means at least n time --> 'aa', 'aaa'
{n,m) -->a{2,4} --> 'aa', 'aaa', 'aaaa' between n and m

[a-zA-Z0-9#]* --> We can take char any number of time including zero times
[a-zA-Z0-9#]+ --> We can take char any at least one time or any many time
[a-zA-Z0-9#]  --> Exactly once 
[a-zA-Z0-9#]? --> One time or Zero Time but not many times

4. Symbols:
^ --> Cap symbol used to check start with Eg: re.search('^Learn',OriginalString) --> Mens whether original string starts with 'Learn'
$ --> $ symbol used to check ends with eg:    re.search('txt$','abc.txt')

"""

import re
pattern='a{}'
str='a7b@k9 zA.aacaaaa'
matcher=re.finditer(pattern,str)
count=0
for match in matcher:
	count=count+1
	print(f"{match.start()}...{match.end()}...{match.group()}")
print(f"Count of Matches {count}")

"""
Regular Expression: If we want to represent a group of string according to a particular format/pattern, then we should go for Regular Expression.

Regular Expression is a declaration mechanism to represent group of string according to a particular pattern.

Example:
	  1. Write regular expression to represent all mobile Numbers.
	  2. Write regular expression to represent all email id's.

Application of Regular Expressions:
1. Patten matching applications
- ctrl + f in windows
- grep in linux

we have module : re in pyton
re module  contains several functions

[abc] --> one char match means can any of these a or b or c

"""
import re

pattern=re.compile('ab')  ## compiling  string into pattern object
#pattern=re.compile('[a-z]')
str='abaababa'
matcher=pattern.finditer(str)  ## Return iterator

for match in matcher:
	print(match.start(),match.end(),match.group())            ## Give start index of each matching, end method will give end index + 1


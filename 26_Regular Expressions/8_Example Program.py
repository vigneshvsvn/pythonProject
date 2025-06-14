"""
To Check given identifier is valid or not as per rule.
Rules:
1. Allowed chars are : a-z,A-Z,0-9,#
2. First char should be lower case alphabet symbol from a to k
3. Second Char should be digit divisible by 3
4. Length of identifier should be at least 2.


"""
import re

identifier='a9cd#3'
#identifier='z6b78'
pattern='[a-k][0369][a-zA-Z0-9#]*'
matcher=re.fullmatch(pattern,identifier)
if matcher is not None:
	print(f"Given Identifier {matcher.group()} is Valid")
else:
	print(f"Given Identifier {identifier} is inValid as per rule {pattern}.")



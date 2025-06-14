"""
re.sub(pattern search, replacement string, Original String)

"""

import re
pattern="\d"
#pattern='a7b@k9 zA.aacaaaa'
replacePattern='#'
str='a7b@k9 zA.aacaaaa'
target=re.sub(pattern,replacePattern,str)
targetn=re.subn(pattern,replacePattern,str)
print(f"Current String:{str}")
print(f"Replace Patter:{replacePattern}")
print(f"New String:{target}")
print(f"New String:{targetn[0]} and count {targetn[1]}")
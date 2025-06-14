"""
Only for first occurrence
"""

import re
pattern="a{2}"
#pattern='a7b@k9 zA.aacaaaa'
str='a7b@k9 zA.aacaaaa'
matcher=re.search(pattern,str)
if matcher is not None:
	print(f"Match available with  {matcher.group()} at {matcher.start()}")
else:
	print(f'Match is not available for given pattern {pattern}')
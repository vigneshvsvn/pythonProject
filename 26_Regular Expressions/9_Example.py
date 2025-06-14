"""
Mobile Number Validation.

"""

import re

MobileNUmber='+919487420965'
#identifier='z6b78'
pattern='([6-9][0-9]{9})|(0[6-9][0-9]{9})|(91[6-9][0-9]{9})|([+]91[6-9][0-9]{9})'
matcher=re.fullmatch(pattern,MobileNUmber)
if matcher is not None:
	print(f"Given Mobile Number {matcher.group()} is Valid")
else:
	print(f"Given Mobile Number {MobileNUmber} is inValid as per rule {pattern}.")

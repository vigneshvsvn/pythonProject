"""
lazy --> zaly
listen --> silent

if two string are having same char set irrespective of order then it's  called as  anagrams.

"""

s1='listen'
s2='silent'

if sorted(s1) == sorted(s2):
	print(f"Given two strings {s1} and {s2} are Anagram")
else:
	print(f"Given two strings {s1} and {s2} are not Anagram")
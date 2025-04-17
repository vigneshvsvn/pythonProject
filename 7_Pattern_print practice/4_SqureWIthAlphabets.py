"""
n=3
A A A
B B B
C C C

chr(65) --> chr() convert unicode to Alphabet
unicode for "A" is 65
"""

number=int(input("Enter Number:"))
for i in range(number):
	print( (chr(65+i)+' ') * number)
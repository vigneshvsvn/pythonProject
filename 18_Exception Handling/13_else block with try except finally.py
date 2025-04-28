"""
try,except,else,finally

try --> Risky code
except --> handling or alternative code  if exception rose with in try block
else --> it will be executed if there is no exception with in try blcck. 
finally --> resource clean-up activity always executes
"""
from sys import prefix

try:
	print("statement 1.")
	print("statement 2.")
	#10/0
	print("statement 3.")
except:
	print('statement 4.')
	print('Statement 5.')
else:
	print("No Exception  in try blcok.")
finally:
	print("Finally Block.")

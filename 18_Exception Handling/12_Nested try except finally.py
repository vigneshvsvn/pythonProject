"""
We can writer try,except,finally blocks can write inside try block, except block and finally block as well.
try

"""

try:
	print("try 1")
	try:
		10 / 0
		print('try2')
	except:
		print("try 2 Except")
	finally:
		print("try2 Finally")
except:
	try:
		print('try 3 inside Except of try1 ')
	except:
		print('try 3 Except')
	finally:
		print('try 3 Finally')
finally:
	try:
		print('try 4 inside Finally of try 1')
	except:
		print('try 4 except inside finally for try1')
	
	finally:
		print("try 1 finally block finally")
	

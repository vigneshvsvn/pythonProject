"""
Another way to read input from the user other than input().
we have to pass argument from the cmd prompt at the time of python execution.

Real time example: Small File Merger application. Read two files and create new files.

eg: python test.py 10 20 30
10, 20,30  are arguments

how to read we have 'sys' module it's having 'argv' variable which is list type.
	Eg:  python .\7Commandline_Argument.py 10 20 30
	output:
	<class 'list'> ['.\\7Commandline_Argument.py', '10', '20', '30'] 4
	10
	20
	30
"""
from sys import argv
print(type(argv),argv,len(argv))
sum=0
for i in argv[1:]:
	print(i)
	sum+=int(i)
print("Sum of Arguments is : ", sum)


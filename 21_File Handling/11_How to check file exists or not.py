"""
 we need to use an os library.
 isfile() functino
"""
import os.path

if os.path.isfile('abc.txt') :
	with open('abc.txt','r') as f:
		print(f.read())

else:
	print("Given file does not Exists.")

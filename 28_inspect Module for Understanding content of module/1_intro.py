import xml.etree.ElementTree as ET
from inspect import getmembers,isclass,isfunction

#To Check members of ET Module
##print(dir(ET))

## Return list of class in ElementTree module
for (name,member) in getmembers(ET,isclass):
	if not name.startswith('_'):
		print(name)

print("*"*30)
## Return list of functions

for (name,member) in getmembers(ET,isfunction):
	if not name.startswith('_'):
		print(name)



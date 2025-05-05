"""
os Module: Contains several functions related to directories.
1. To know the current directory
	-

"""
import os

print("1. Current Working Directory:",os.getcwd())

# To List only list given directory but not sub directories.
print(os.listdir())
#print(os.listdir('C:\\Users\\Dell\\Desktop\\'))

#To list current direcotry and sub directory : Return list of  tuple with [(directory name, list of directory,list of files) ]
print(list(os.walk('TestDir')))

# To Create Directory
try:
	os.mkdir('TestDir')       # in current dire
	# os.mkdir('C:\\Users\\Dell\Desktop\Python_Directory')  # With Absolute Path
except FileExistsError as msg:
	print(msg)

# To Create SubDirectory
try:
	os.mkdir('TestDir/sub1')
except FileExistsError as msg:                      		
	print(msg)

## To Create all Directory and Sub directory.need to use makedirs()
try:
	os.makedirs('C:\\Users\\Dell\Desktop\Python_Directory\sub1\sub1_1')
except FileExistsError as msg:
	print(msg.filename,msg.strerror)

# To remove Directory only when it's empty
#os.rmdir('C:\\Users\\Dell\Desktop\Python_Directory\sub1\sub1_1')

# to remove all child and parent directory and files
#os.removedirs('TestDir\sub1')

# To Rename the Directory
#os.rename('TestDir/sub1','TestDir/sub1_1')






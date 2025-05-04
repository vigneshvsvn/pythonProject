"""
we need to use
Module: zipfile.
Class Name: ZipFile

To Write:
f=ZipFile(filename,'w',ZIP_DEFLATED)


To Read:
f=ZipFile(filename.'r',ZIP_STORED)  ## ZIP_STORED is default

"""
import zipfile
from zipfile import ZipFile, ZIP_DEFLATED, ZIP_STORED

## Creating Zip files
# f=ZipFile('NewSample.zip','w',ZIP_DEFLATED)
# f.write('abc.txt')
# f.write('abc1.txt')
# f.write('Briyani.jpg')
# print("Zip file created with NewSample.zip ")
# f.close()

## Reading Zip File

f=ZipFile('NewSample.zip','r',ZIP_STORED)
names=f.namelist()
print(names)
print(f.getinfo('abc.txt'))
for eachname in names:
	print(eachname)
	f1=open(eachname,'r')
	#print(f1.read())
	f1.close()



import os.path

from select import error

fname=input("Enter File name:")
if os.path.isfile(fname):
	print(f"Given File {fname} exists.")

	lcount=0
	wcount=0
	ccount=0
	f=open(fname,'r')
	for eachline in f:
		lcount+=1
		#print(eachline,end='')
		num_words_in_CurrentLine=len(eachline.split())     ## convert string into a list and finding a length list
		wcount=wcount+num_words_in_CurrentLine
		num_Chars_in_CurrentLine=len(eachline)             # len of strings of eachline
		ccount=ccount+num_Chars_in_CurrentLine

	f.close()
	print("Number of Lines:",lcount)
	print("Number of Words:",wcount)
	print("Number of Chars:",ccount)

else:
	print(f"Given File {fname} does not exists.")


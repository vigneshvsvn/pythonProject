"""
with statement:   After completing the required operation automatically close the file.

Normal Way:
f=open('abc.txt','w')
# perform action
f.close

Using With:
with open('abc.txt','w')  as f:
	required operation

"""
with open('abc.txt','r')  as f:
	data=f.read()
	print(data)
	print("Inside With statement File Closed?", f.closed)

print("Outside with statement Closed?",f.closed)

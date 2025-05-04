fname=input("Enter File name:")
f=open(fname,'w')
while True:
	data=input(f"Enter Data to write to {fname}:")
	f.write(data+'\n')
	option=input("Do you want to add Some more data[Yes or No]:")
	if option.lower()=='no':
		break

print("Data written completed.")
f.close()


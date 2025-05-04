"""
1.f.write(str)
2.f.writelines(list of Strings)

"""
list=['Vignesh','Priya','Privika']
f=open('abc.txt','w')
f.write("Hello Vignesh !! ")
f.write("How are you?\n")
f.write("Learning Python is Good.\n")
f.writelines(list)
f.close()
print("Data written to file successfully")
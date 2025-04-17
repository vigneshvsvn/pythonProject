l=[0,1,2,3,4,5,6,7,8,9,10]
print("Actual List:",l)


evenList=list(filter(lambda n:n%2==0,l))
print("Even List:",evenList)


oddList=list(filter(lambda n:n%2!=0,l))
print("Odd List:",oddList)


divisibleBy3=list(filter(lambda n:n%3==0 and n%2!=0 ,l))
print("divisibleBy3 and Odd:",divisibleBy3)

namelist=['Vicky','Priya','Privika','Gnanam','Mahesh']
startswithP=list(filter(lambda name: name[0]=='P',namelist))
print("Names starts with 'P' : ",startswithP)
namelendivby5=list(filter(lambda name: len(name)%5==0,namelist))
print("namelendivby5 : ",namelendivby5)
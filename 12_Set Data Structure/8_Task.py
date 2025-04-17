## Remove Duplicate


lst=[10,20,30,40,50,20,30]
print(lst)

##Using Loops  Way 1
lst1=[]
for i in lst:
	if i not in lst1:
		lst1.append(i)
print(lst1)

## By using Set is the essay way2 
lst2=list(set(lst))        	
print(lst2)

## read string from key board and find list of vowels
word=input("Enter the Word:")
s=set(word)
s_v={'a','e','i','o','u'}
result=s.intersection(s_v)
print(result)

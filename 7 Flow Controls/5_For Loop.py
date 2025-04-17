"""
For Loop mainly used to iterate elements for sequences like String , LIst, Tuple,dict ,range ...
Syntax :
for variable_name in sequence:
statements
"""
## print 50 to 70
for i in range(50,71):
	print(i)
## to print 50 70 with step 2
for i in range(50,71,2):
	print(i)
## to print each char in string with it's index
name="Vigneshkumar"
index=0
for element_of_name in name:
	print(f"The character in index {index} is {element_of_name}")
	index=index+1
############ print 10 to 1
for i in range(10,0,-1):
	print(i)
#######Print sum of numbers present in the list
#lst=eval(input("Enter the list :"))   ## input itself as list --> [1,2,3,4,5]
lst=input("Enter list of number separate with ',' : ").split(',')  ## input as string 1,2,3,4,5
sum=0
for element_of_lst in lst:
	sum=sum+int(element_of_lst)

print("Sum of numbers in the List is ",sum)

### More easy way to use sum function
##print(sum(lst))
## 0 to 9 convert to Word
from itertools import product

list=['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','seventeen','Eighteen','Nineteen']
list2=['','','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
number=int(input("Enter Number between 0-99:"))
output=0
if number < 0:
   print("Given Number is Negative")
elif number==0  :
	print("Zero")
elif number<=19:
	print(list[number])
elif number<=99:
	output=list2[number//10]+list[number%10]
	print(output)
else:
	print("Given number is out of our scope")


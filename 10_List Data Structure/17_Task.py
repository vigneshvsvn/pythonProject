"""
Program to find unique vowels in the Word
"""
from xml.sax.saxutils import escape

vowels=['a','e','i','o','u']
word=input("Enter String to find Vowels:")

#### Using For Loop
lst1=[]
for each_element in word:
	if each_element in vowels:
		if each_element not in lst1:
			lst1.append(each_element)
print('lst1:',lst1)


####   Using Comprehension
lst2=[ each_element for each_element in vowels if each_element in word]
print("lst2:",lst2)


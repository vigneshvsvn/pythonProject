"""
Removing spaces from the string
1.lstrip() --> To remove at beginning of the string. Left side spaces will be removed
2.rstrip()  --> To Remove at end of the String. Right side spaces will be removed
3.strip()  --> To remove beginning and end of the string. Both sides it will remove the spaces.
"""

city=input("Enter your City: ")  ## If we are giving with space's then condition will not match SO it will flow to else always.
scity=city.strip()
if scity=='Hyderabad':
	print("Hello Hyderabadi....Aadab")
elif scity=='Chennai':
	print("Hello Madarasi ... Vanakam!")
elif scity=="Bangalore":
	print("Hello Kanadiga....Namaskara !!")
else:
	print("Invalid City. Assuming vadakan and Namaste")

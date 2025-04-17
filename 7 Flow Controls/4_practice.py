##Odd Numbers Between Min and max
min_number=int(input("Enter Min Number:"))
max_number=int(input("Enter Max Number:"))
i=min_number
while i <= max_number:
	if i % 2 != 0 :
		print(f"Number {i} is Odd.")
	i=i+1

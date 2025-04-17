from wave import Wave_write

str="Vigneshkumar"
print("Given String:",str)

##Way 1
print("even Index chars:",str[::2])
print("Odd Index chars:",str[1::2])

# Way 2
odd_lst=[]
even_lst=[]
i=0
while i <len(str):
	if i%2==0:
		even_lst.append(str[i])
	else:
		odd_lst.append(str[i])
	i=i+1
print("even List",''.join(even_lst))
print("Odd List:",''.join(odd_lst))

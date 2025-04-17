"""
When x is multiple for 3 then Skip   using Continue statement
continue will skip that particular loop instead of whole loop, it continues next iterations
"""
x=0
while x<=20:
	x += 1
	if(x%3 == 0):
		continue
	print(x)
	

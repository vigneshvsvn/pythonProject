"""
Else can be used with else block as well.

When to use else with loop block.

Loop with out break statement execution then only else part will execute. Means loop should  fully execute without break.

for
else

while
else

try
except
else
finally
"""

cart=[10,20,30,40,50,600]
for i in cart:
	if i > 500:
		print("We can't place this order as we Insurance required ")
		break
	print(f"Processing Item {i}")
else:
	print("All Items Processed successfully")
	
def outer():
	print("Outer Function Started to Execute...")
	def inner(): ## Defined inner function within outer Function
		print("Inner Function Execution Started...")

	return inner      ## returning Inner function reference 

f1=outer()
#f1()

def function(fname):
	fname()

function(f1)



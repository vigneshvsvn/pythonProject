""""
Function Aliasing:
- In Python everything is Object even function also Object
- Giving another reference name to the same existing function.
- We can call function with multiple names
- If we delete one reference, still we can call using another Function.

Nested Function:
- One Function declared inside another function
"""

def wish(name):
	print('Hello,',name)

print(wish)   ## wish is the function object
print(id(wish))  ## Address of the Object

greeting=wish ## Function aliasing. So for same Object we have two reference variables(in our case wish and greeting).

print(greeting)
print(id(greeting))

wish('Vignesh')
greeting('Priya')

## Nested Functions
print("**************Nested Function  **************")
def outer():
	print("Outer Function Started to Execute...")
	def inner(): ## Defined inner function within outer Function
		print("Inner Function Execution Started...")

	inner()
	print("Outer Function Completed.")

outer()

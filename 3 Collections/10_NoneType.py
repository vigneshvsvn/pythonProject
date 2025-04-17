""""
None means nothing, no values associates.

it's equivalent to Null in java and other languages
to make object eligible for garbage collection.

if function is not return anything then it's none
in entire python application there will be only one None Object available 
"""

a=None
print(type(a),a)


def m1():       ## This method is not returning any values, if we call the function it will return None
	a=10


print(m1())

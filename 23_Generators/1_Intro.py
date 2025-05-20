"""
Generator:  Special type of function to Generate a sequence of Values.

keyword: generator used 'yield' keyword to  return generated values.

Collection vs Generator:

In

"""
#List  --> All values objects created and store as list.
# For each element, one object will create.
# There will Memory Utilization issue Eg: range(10000000)   . Because of Huge number of object need to store in Heap
l=[ x*x  for x in range(10) ]
print(type(l))
print(l)
print(l[0])     

#generator if we use tuple comprehension, then it will return Generator Object.
# Generator will not create all objects but at the same time.
# WHen we call next then only an next object will create. Here not all objects at time.
# on demand, we generate by using next function.

g=(x*x  for x in range(10) )
print(g)
print(type(g))
while True:
	print(next(g))
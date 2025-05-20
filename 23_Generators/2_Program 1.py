def mygen():
	yield 'A'
	yield 'B'
	yield 'C'
	yield 'D'
g=mygen()
print(type(g))

# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

#TO avoid StopIteration, we can use it for loop
for x in g:
	print(x)

## Example 2: Create Generator of first n numbers

def mygenerator2(n):
	i=1
	while i <=n:
		yield i
		i=i+1

g1=mygenerator2(100)

for x in g1:
	print(x)


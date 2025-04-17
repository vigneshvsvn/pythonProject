"""
- range is python in build datatype.    it's sequence of numbers.
- As it's sequence of number it's ordered.
- slicing and indexing are allowed 
range(end)          --> one argument passing     eg: range(n) --> range from 0 to n-1
range(start,end)    --> two argument passing 
range(start,end,step)    --> three arguments including step
range is immutable
"""

r=range(5)  ## represent  0 to 4
print(type(r),r)
print(3*"#"+"one argument"+3*'#')
for i in r:
	print(i)

print(3*"#"+"two argument"+3*'#')
r=range(1,6)
for i in r:
	print(i)

print(3*"#"+"three arguments with step"+3*'#')
r=range(1,10,2)
for i in r:
	print(i)
print(3*"#"+"decrement with step"+3*'#')
r=range(10,1,-2)
for i in r:
	print(i)

print(3*"#"+"Indexing and Slicing "+3*'#')
r=range(1,10)
print(r[0],r[-1])             ## indexing
r1=r[1:5]                     ## slicing
for i in r1:
	print(i)

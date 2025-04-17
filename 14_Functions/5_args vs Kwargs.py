"""
*args    --> Variable length arguments.
	Exmaple: def f1(*n):        always consider as Tuple
			  pass

**kwargs   --> Variable length  Key word arguments.
	Example: def f1(**n)
			--> It will consider as dictionary
"""

def f1(*args):
	print(args)

def f2(**kwargs):
	print(kwargs)     ## kwargs will consider as dictionary as we used double **. One * for Key and another * is for Value.

def f3(*m,**n):
	print(m)
	print(n)

f1()
f1(10)
f1(10,20,30)

f2()
f2(name='Vignesh',RollNum=10)


f3(10,20,30,a=10,b=20)

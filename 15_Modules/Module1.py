pi=3.14

def areaCircle(radius):
	print("From Module 1")
	return pi*radius*radius

def sum(a,b):
	return a+b

if __name__ == '__main__':
    print("Direct Exucution")
else:
	print("InDirect Execution because of Import Statement")


def f1():
	print("Function 1 is executing")
def f2():
	print("Function 2 is executing")
def f3():
	print("Function 3 is executing")



if __name__ == '__main__':
	f1()
	f2()
	f3()

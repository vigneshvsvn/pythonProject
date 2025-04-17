"""
Constructor is  special Method in Python.
	- Name of constructor is always fixed. Which __init__(self)
	- When ever we are creating Object Constructor will be executed automatically. Only once per object. If we create 3 objects then it will execute constructor 3 times.
	- Main Objective of Constructor:
		- To Initialization and declaration of Instance variable.

Note: Constructor is not Mandatory. Even if we are not creating constructor python will provide default constructor.
	  If we define Multiple constructor then only latest will consider. OverLoading is not there in the Python.

"""
class Test:
	def __init__(self):         ## as there is no other arguments it's No Argument constructor.
		print("Constructor Execution...")

t1=Test()
t2=Test()
t3=Test()
t1.__init__()      ## we can call constructor explicitly but no new object create. It's just act like normal method.

class Student:
	def __init__(self,name,rollno,marks):
		self.name=name
		self.rollnum=rollno
		self.marks=marks

s1=Student('Vignesh',70,95)
print(globals())

class Test2:
	def __init__(self):
		print("Constructor 1")

	def __init__(self,x):            ## If we create two Constructors then python will consider only latest constructor
		print("Constructor 2")

##test2_1=Test2()     # Test.__init__() missing 1 required positional argument: 'x',It's not possible to create Object with No arg constructor as we one Arg constructor.
test2_2=Test2(10)


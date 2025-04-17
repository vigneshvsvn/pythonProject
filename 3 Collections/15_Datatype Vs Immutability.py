"""
Mutable: means changeable
Immutable: means non changeable
All Fundamental datatypes(int,float,bool,str,complex) are Immutable.
  - Once we create object we can't perform any changes in that object.
  - If we are trying to perform any changes then new object will create with those changes. It is called immutability.
  - If we change always new object only will create.
  - Every thing in object in python.
  		x=10
		X is reference for object 10. using id() we can print address of the object
- complex type will not use same reference object.
Why Immutability is required  ?
- PVM is responsible for object creation.
- To achieve Object reusable to improve memory usage,
- performance improvement. Object creation is costly action now we used existing object itself so performance is better here.
- is operator used to compare both are point same object or not

Problem of Immutability?

"""

x=y=10
print("Address of x:",id(x))
print("Address of y:",id(y))
x=10+2
print("New address of X:",id(x))

## now object 10 will not have any reference to  it. So it's eligible for Garbage Collection.
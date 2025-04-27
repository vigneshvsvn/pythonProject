"""
Abstraction:    Something is not having completeness. It's just Outline without internal Implementation.

1. Abstract Method : Method which has only  declaration without implementation.
					 Child class is responsible for implementing the method.

	Example:
	@abstractmethod
	def getNoOfWheels(self):  ## we have onl
		pass

	-  We need to declare explicitly with @abstractmethod which is availble in abc Module.

2. Abstract Class: Partially Implemented Classes are called Abstract class.
				Abstract class need to inherit class ABC is mandatory.
				ABC --> Abstract Base Class

Abstract class is the child of ABC class.
Abstract class with one abstract Method then object creation is not possible.

"""
from abc import *
from symtable import Class

class Vehicle(ABC): ## Abstract class not implemented fully.
	@abstractmethod
	def getNoOfWheels(self):  ## Only declaration and not implemented.
		pass
class Bus(Vehicle): # Child class implemented concrete with implementation
	def getNoOfWheels(self):
		return 6

class Auto(Vehicle): # Child class implemented concrete
	def getNoOfWheels(self):
	 	return 3
	pass

b=Bus()
a=Auto()
print("Number of Wheel in Bus:",b.getNoOfWheels())
print('Number of Wheel in Auto:',a.getNoOfWheels())





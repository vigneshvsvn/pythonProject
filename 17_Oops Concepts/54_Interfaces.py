"""
Interface:  Abstract Class Contains only  abstract Methods then we can call it interface like other programming languages like Java.
 - Interface act as service requirement specification

- Officially not available in  Python. We can use using Abstraction we can implement in directly.
"""
from abc import ABC, abstractmethod

## Class Test will not act a Interface as we have concrete method m1 as well.
class Test(ABC):
	def m1(self):
		print("Method 1")

	@abstractmethod
	def m2(self):
		pass

### Class Test 1 is act as interface. as Abstract class has only abstract Methods.
class Test1(ABC) :
	@staticmethod
	def m1(self) :
		print("Method 1")

	@abstractmethod
	def m2(self) :
		pass


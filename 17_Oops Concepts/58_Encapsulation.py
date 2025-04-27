"""
Encapsulation: The process of required things into single unit.  Z



In Programming: Grouping of Data(name,Rollnum,Marks,Age) + Behaviour (Methods read(),getInfo())
Example:    every Class is example of encapsulation.

if any component follows data Hiding + abstraction  such component call Encapsulation.

- Hide data behind our methods
Advantages:
1. Security because we are not going to show our internal implementation.
2. Enhancement is Easy:
3. Modularity and Maintainability  :

Disadvantage:
1.  Performance will reduce as we do validation at each stage.
2. Increase length of code due to multiple validations.


"""


class Account :
	def __init__(self, initial_balance) :
		self.__balance = initial_balance  ## data hiding

	def getBalance(self) :
		## Implement Validation and authentication.
		return self.__balance

	def deposit(self, amount) :
		## Validation and authentication
		self.__balance += amount

	def withdraw(self, amount) :
		# validations
		self.__balance -= amount

"""
DataHiding: Hide our internal data to outside world.
Advantage:
1. Security --> No one from outside  allowed to access/modify our internal data.

"""

class Account:
	def __init__(self,initial_balance):
		self.__balance=initial_balance

	def getBalance(self):
		## Implement Validation and authentication.
		return self.__balance


a=Account(5000)
print("Balance Amount:",a.getBalance())
##print(a.__balance)       Not possible as it's private Method.
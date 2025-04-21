class Customer:
	"""
	This class developed by Vigneshkumar and describes bank operations.
	"""
	bankName="TMB"
	def __init__(self,name,balance=0.0):
		self.name=name
		self.balance=balance


	def deposit(self,amount):
		self.balance+=amount
		print(f"Your account Credited with {amount} and your new balance amount {self.balance}")

	def withdraw(self,amount):
		if amount < self.balance:
			self.balance-=amount
			print(f"After withdraw {amount}, your available balance is {self.balance}")
		else:
			print("Insufficient Balance. Please check your Balance")



print("Welcome to",Customer.bankName)
name=input("Enter Your Name:")
c=Customer(name)
while True:
	print(" d for Deposit \n w for Withdraw \n e for Exit")
	option=input("Please choose your Option:").lower()
	if option=='d':
		amount=float(input("Enter Amount to Deposit:"))
		c.deposit(amount)
	elif option=='w':
		amount=float(input("Enter Amount to withdraw:"))
		c.withdraw(amount)
	elif option=='e':
		print("Thank you for Bannking with",Customer.bankName)
		break
	else:
		print("Invalid Option selected, please enter valid options")





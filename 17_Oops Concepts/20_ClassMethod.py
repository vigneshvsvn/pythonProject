"""
Inside Method implementation only use static variable or class variable called class method.
	- Independent of Objects
	- mandatory to use @classmethod decorator
"""

class Bird:
	wing=2
	@classmethod
	def fly(cls,name):
		print(f"{name} flying with {cls.wing} wings")


Bird.fly("Privika")
Bird.fly("Vignesh")


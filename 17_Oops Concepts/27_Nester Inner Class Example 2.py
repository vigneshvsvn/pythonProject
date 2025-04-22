"""
Automatically Create Object of inner class when we create object of outer class.

"""
class Human:

	def __init__(self,name):
		self.name=name
		self.head_obj=self.Head()

	def info(self):
		print("Hello",self.name)
		self.head_obj.talk()
		self.head_obj.brain_obj.think()

	class Head:
		def __init__(self):
			self.brain_obj=self.Brain()

		def talk(self):
			print("Talking.....")

		class Brain:
			def think(self):
				print("Thinking....")


obj=Human("Vignesh")        # when create Human object automatically Head Object will create as in constructor we are creating Object.
obj.info()


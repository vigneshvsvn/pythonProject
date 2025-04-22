class Person:
	def __init__(self,name,dd,mm,yyyy):
		print("Person Object Creation.....")
		self.dob_obj=self.Dob(dd,mm,yyyy)
	def info(self):
		self.dob_obj.display()

	class Dob:
		def __init__(self,dd,mm,yyyy):
			print("Dob Object Creation.....")
			self.dd=dd
			self.mm=mm
			self.yyyy=yyyy

		def display(self):
			print("Date of Birth:{}/{}/{}".format(self.dd,self.mm,self.yyyy))


p=Person("Vignesh",13,'07',1991)
p.info()
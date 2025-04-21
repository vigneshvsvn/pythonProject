class Test:
	count=0
	def __init__(self):
		Test.count+=1

	@classmethod
	def getNoOfObjects(cls):
		print("The Number of Objects Created is",cls.count)


Test.getNoOfObjects()
Test()
Test()
Test()
Test.getNoOfObjects()

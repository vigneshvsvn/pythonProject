"""
setup() --> for each test one time run.
test() --> can use our own naming for test method, but it should start with test. Eg:test1(), test2()..
teardown() --> for each test one time run.

setUpClass(cls) --> this class method used to do common setup for all test. Only once run.
tearDownClass(cls) --> this class method used to close common setup  done using setUpClass. only once it will run

"""

import  unittest

class TestCaseDemo(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		print("setUpClass Method")

	def setUp(self):
		print("Setup method executing")

	def test_Method1(self):
		print("Executing Test case 1.")

	def test_Method2(self) :
		print("Executing Test case 2.",10/0)

	def tearDown(self):
		print("Executing Teardown method.")

	@classmethod
	def tearDownClass(cls):
		print("tearDownClass method")

#unittest.main()
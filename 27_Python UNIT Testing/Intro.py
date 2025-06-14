"""
Testing:
1. Unit Testing:  The process of testing particular unit (individual component) called unit testing.
2. Integration Testing: After integrating all units or all individual components and testing full test of final product called Integration test.
						 Full application Testing.

Test Scenario:
1. Checking login functionality
2. Testing inbox functionality
3. File generation test

Test Case:
1. with valid user name and valid password
2. with valid username and invalid password
3. invalid user name and valid password
4. invalid user and password
5. blank user id and password

Test Suite:
group multiple test case into suite. Execute the suite to cover all test cases.

Module name: unittest
Class Name: TestCase
Methods:
	1.setup() --> required environment setup
	2.test() --> actual test
	3. tearDown() --> Clean up activities, close browser, close connection..

class TestCaseDemo(TestCase)

"""
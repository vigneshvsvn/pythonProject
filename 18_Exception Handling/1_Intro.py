"""
Two types of Possible Errors:
1. Syntax Error:
	- Because of invalid syntax usage. Eg: Missing colon, parenthesis...
	- Programmer is responsible for fixing this issue.

2. Runtime Error also called Exceptions:
	- Because of Invalid input, Memory problem, Logic Mistake, DB connection issue....
	- Eg: divisible by Zero
	- ValueError, ZeroDivisionError, FileNotFoundError
	- Exception Handling concepts only applicable for Runtime errors.
	- Unwanted and unexpected event occurs that disturbs the normal flow of the Program called Exceptions.

Purpose of Exception Handling?
- To achieve graceful Termination, and we should not block our resources.

What is the Meaning of Exception Handling?
- It does not mean fixing or exceptions.
- Defining alternative to continue the rest of program normally even we have abnormal exceptions.


Default Exceptions Handling:
- Every Exception is a class in python.
- Once an Exception raised object will create for the respective Exception class.
  PVM looks for handling code if not there then program will terminate and print the Exception in the Console.

Python Exception Hierarchy:
Parent class: BaseException
Child class for BaseException: 1. Exception 2. SystemExit 3. GeneratorExit  4. KeyBoardInterrupt

Child for Exception class:
1. ArithmeticError
	- ZeroDivision Error
	- OverFlowError
	- FloatingPointError
2. LookupError
	- IndexError,
	- KeyError
3. OsError:
	- FileNotFoundError
	- TimeOutError
	- InterruptedError
	- PermissionError
4. AttributeError
5. EOFError
6. NameError
7. TypeError
8. ValueError

"""
print("Hello")
print(10/0)
print("Hi")
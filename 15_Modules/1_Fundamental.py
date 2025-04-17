"""
What is Module:
	Group of variables , functions, classes....saved to a python file. That file is call Module.
	Each and every .py file called as Module.

Advantage:
	- No Duplicate Code increase code reusability.
	- Concise Code as length of code reduced so increase readability.
	- Maintainability is Easy. In Future any changes are going to do. Only one place need to change.

	Eg:  are two modules.
	Module1.py
	Module2.py

Importing Ways:

1. import Module_name
   Module_name.varialblename   ## how to use.

2. import Mudule1,Module2,...  ## import multiple module in single line

3. import Module1 as m1,Module2 as m2  ## giving alise for multiple module.

4. from Module1 import pi,areaCircle  ## import particular member

5. from Module1 import pi as p ,areaCircle c  ## giving alias to Member

6. from Module1 import *  ## import all members  

when ever we use other modules, compiled version of that module stored in __pycache__ internally for better performance.
As no need to compile many times.
( D:\Learning\python\BharathThippireddy\pythonProject\15_Modules\__pycache__) --> Module1.cpython-310.pyc

"""
import Module1
print(Module1.pi)
radius=int(input("Enter radius of Circle:"))
areaOfCircle=Module1.areaCircle(radius)
print("Area of Circle:",areaOfCircle)
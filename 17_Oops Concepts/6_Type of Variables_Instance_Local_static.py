"""
1. Instance Variables:
	- Value of variable vary to object to Ojecrt called Instance  Variable.   self.variable_names are instance variable


2. Static Variables:
	- Also called as class level Variable.
	- Value of variable not vary object to Object then use static Variable.
	  Else for each Object we need to create separate copy which will use unnecessary Memory.
	- Only one copy will be created at class Level. Same copy will be shared to all objects of the Class.

3. Local Variables:
	- Method level Variable used for temporary purpose.

"""
class Student:
	school_name="VSVN PolyTechnic"    ## Static Variable: value will not change shared among all object.
	def __init__(self,name,rollNum):  ## name and rollNum are local Variable. only accessible for the method not outside.   used for temporary purpose. 
		self.name=name                ## self.name and self.rollnum are instance variable. Value changes object to object
		self.rollnum=rollNum
		i=10                          ## this also local variable for temp requirement
	
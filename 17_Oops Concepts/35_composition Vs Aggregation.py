""""
Composition:      Container Object and Contained Objects are strong association. Without Container object Contained Object can't be exist.

Aggregation:   Container Object and Container Objects are weak association. Without Container  object contained Object can be existing.
"""

## Composition: without university  object Department Object can't be created.

class University:
	def __init__(self):
		self.dept=self.Department()

	class Department:
		pass
u=University()

## Aggregation;  Eg: without Department Object professor Object Can Exists.
class Professor:
	pass

class Departments:
	def __init__(self,professor):
		self.professor=professor
professor=Professor()
csDepartment=Departments(professor)
mcaDeparment= Departments(professor)
	
	
"""
+ --> __add__(self,other)
- --> __sub__()
* --> __mul__()
/ --> __div__()
// --> __floordiv__()
% --> __mod__()
** --> __pow__

+= --> __iadd__()
-= --> __isub__()
< --> __lt__()
<= --> __le__()
> --> __gt__()
== --> __eq__()
!= --> __ne__()

Refer Pyton doc for Magic methods.

"""

class Student:
	def	__init__(self,name,marks):
		self.name=name
		self.marks=marks

	def __gt__(self, other):
		if self.marks > other.marks:
			return True
		else:
			return False

class Employee:
	def __init__(self,name,salPerday):
		self.name=name
		self.salPerday=salPerday

	def __mul__(self, other):
		return self.salPerday*other.numOfWorkDays

class Timesheet:
	def __init__(self,name,numOfworkDays):
		self.name=name
		self.numOfWorkDays=numOfworkDays



s1=Student('Vignesh',100)
s2=Student('Ravi',90)
print(s1>s2)               ## over loading > and < operator by Magic Methods

e1=Employee('Vignesh',1000)
t1=Timesheet('Vignesh',30)
print('Monthly Salary:',e1*t1)              ## magic Method should be implemented on first class. So here we need to do at Employee class
#print('Monthly Salary:',t1*e1)    ## it will not work as we implemented magic method only in Employee class.  If we need reverse order then we need to implement in Timesheet class as well.


"""
In General Package : Group of related items consider as package.
Python Packages:   Group of Related Modules,subpackages  called Package.
					Any folder or directory which contain __init__.py  consider as python package.



 Advantages;
	- unique identification of Modules. Means sub package can have same module name.   To resolve conflicts 
	- Modularity of the application is going to improve.
	- readability of the application is going to improve.
	- Maintainability of application is easy.

Relationships:
Function: Group repeatedly required  line of codes
Module : Group of members (variable,function,class ......)
package : Group of multiple Modules
library : Group of packages 

 """
import loan.vehicleLoan.TwoWheeler  as t
from loan.homeloan.flatLoan import f1
t.f1()
f1()

##D:\Learning\python\BharathThippireddy\pythonProject\16_Package\loan\vehicleLoan\TwoWheeler.py


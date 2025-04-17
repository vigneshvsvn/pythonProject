""""
import math      --> import module and call members with math.<Member Name>
import math as m   --> import module and  given alise to it and call m.<member name>
from math import pi,pow --> import only required members
from math import *  --> all members included

"""
from math import *

r=eval(input("Enter Radius of Circle:"))
print("Area of Circle:", pi*r*r)
print("Area of Circle:", pi*r**2)
print("Area of Circle:", pi*pow(r,2))

print(dir(math))   ### dir(module name ) will give list of all members present in the math Module (variable, functions )

                                                                       
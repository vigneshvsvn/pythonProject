"""
To access any variable or function. Every time we need to call with module name.
so it's very long to type.

Example:       Once we created alise we can't use original name. We will get error.
	  import Module1 as m1
		print(m1.pi)  ##

To access variables or function... with out using ModuleName.
We need to use from import

from Modulename import *                     ## * means import all members from the module.
from Modulename import pi,areaCircle         ## Mentioning explicitly members what are required from Module  (Eg: only pi and areaCircle)

"""

import Module1 as m1   ## created alias for Module1 as m1 . After Creating alise we should be able use actual module name to call.
from Module2 import *  ## from import allows us to use function name directly with out representing Module name.

print(m1.pi)           ## We can use with alias name m1 instead of full module name.

print("Ares of Rectangle:",areaofRect(10,20))       ## from import, so we can use areaofRect() directly. Instead of Module2.areaOfRect()


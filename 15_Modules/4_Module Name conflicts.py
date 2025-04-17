""""
   As areaCircle() available in both Modules, it will consider only latest Module.

   How to Resolve ?
   Solution 1:    use Module Import method
   import Module1
   import Module2
   Module1.areaCircle()
   Module2.areaCircle()

   Solution 2 : give aliase  to Member to differentiate 
   from Module1 import areaCircle as a1
   from Module2 import areaCircle as a2
   a1.areaCircle()
   a2.areaCircle()
"""

from Module2 import *
from Module1 import *

print("Area of Circle:",areaCircle(10))    ## As areaCircle() available in both Modules, it will consider only latest Module.


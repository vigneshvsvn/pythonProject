""""
Extra Members added by Python. To maintain

__doc__ --> To maintain doc strings in the Module
__file__ --> To Hold File name of Module
__name__ -->  Very Important 
__loader__ -->
__package__ -->  To find the module related to which package
"""
from os import *
print("dir():",dir())
## print(__doc__)   Print all documentation  which we have given inside triple Quote
print("*"*50)
print("File Neme absolute path (__file__): ",__file__)
print("*"*50)
print(getcwd())
print(__name__)


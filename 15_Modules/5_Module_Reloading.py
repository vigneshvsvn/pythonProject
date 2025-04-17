""""
If we import multiple times, it will load only one time.

If updated copy not available in __pycache__ folder then we need to reload the modules

how to reload() function which is not  builtin need to import importlib module

"""
from importlib import reload

import Module1
reload(Module1)

print(Module1.sum(5,4))


"""
inspect: To perform inspection we need inspect module.
	if we want to know from where the request came either class, function , Module.

"""

import inspect

def getInfo():
	print(inspect.stack()[1][3])
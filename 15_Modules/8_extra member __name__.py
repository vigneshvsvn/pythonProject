""""
__name__ -->
		if it's executed directly then __name__ reruns __main__        Direct execution: py Module1.py
		if it's executed indirect  then  __name__ returns ModuleName   Indirect import Module1 from other Module.


"""
import Module1    ## all prints execute indirectly due to import.   __name__  --> return Module1

print("Current  Module")
print(__name__)     ## direct execution  so it will return __main__
Module1.f1()
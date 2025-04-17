"""
del means delete.
Eg: x=10
after using this variable x,  Assume x is no more required, but still object 10 will be in the memory.

To Clean it up we del reference x. So Object 10 become eligible for Garbage Collection,

It's used to Improve Free Memory.
"""
x=10
print(f"Value of X={x}")
del x
print(x)
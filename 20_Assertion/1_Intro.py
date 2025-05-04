""""
Bug:Deviation between expected output vs Original output called Bug.
Debugging: Identify the issue and fixing the bug called Debugging.

Common Way of Debugging:
By Using print statements. But these are extra code added part of the program. After fixing the bug all these print statements
need to be deleted.

As an alternative to these print statement, we have assertion concepts.
Advantage:
If we use assertion after fix, we don't need to delete these statements. We can enable and disable assertions.

Types of Assert:
1. Simple Version:
Syntax: assert <conditional expression>
If the condition fails, it will through an Assertion error

2. Augmented Version: More simpler version
Syntax: assert <conditional expression>, message

If the condition fails, in addition to an Assertion error message will be printer.

How to Disable assertion in Python:
by using -O option.

Example: 	python -O test.py

"""

def squareit(x):
	return x*x

assert squareit(2)==4,'The Square of 2 should be 4'
assert squareit(3)==9,f'The Square of 3 should be 9 '
assert squareit(4)==16,'The Square of 4 should be 16'

print(squareit(2))
print(squareit(3))
print(squareit(4))


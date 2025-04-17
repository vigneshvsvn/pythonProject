"""
In Standalone applications we may need to get instructions from user and print out put to the console.
We will used input() to get input from user
and print() to print in output console to user
"""
print()
print("Hello" * 3)
print("All the power \n is with you")
a,b=10,20
print(a,b)
print(a,b,sep=',')      ### both value will get separate with given delimeter and data given as separator


name="John"
marks=95.5

print("Name is",name,"Marks are",marks)
#print("Name is %s, Marks are %f",%name)
print("Name is {},Marks are {}".format(name,marks))
print(f"Name is {name} and Marks are {marks}")

## %i interger , %s string , $f float



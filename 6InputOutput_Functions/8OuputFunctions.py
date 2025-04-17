"""
Output statement : print()
form 1: print() --> print new line character (\n). one blank line
form2:  print(str) --> string as argument
form3: print(a,b,c,d) --> Any number of argument can be printed by separating with ',' comma
form4: print(a,b,c,d,sep=',')  --> sep operator to give our own separator
form5: print(a,b,c,d,end='') --> automatically new line will be added at end. Default it will got to next line for print. To change that we can own


"""
print("Vignesh\nkumar")
print("Priya"+"Dharsini")
print()     ## Blank line 
print("\tPrivika")

a,b,c=10,20,30
print("Values are ",a,b,c)   ## print space between the arguments default
print("Values are ",a,b,c,sep=',')   ##  Own separation of arguments

print("vignesh",end='')  ### after printing dont insert \n, we specified end='' empty string 
print("Kumar")



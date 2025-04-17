"""
1. Empty Dictionary : d={}  or d=dict()
2. If we know data already d= {100:'vignesh', 200:'Priya' ,,,}
3.  Other Collections to Dictionary 
	lst=[(1,30),(2,40),(3,50)]
	d=dict(lst)
4. By using Dynamic Input

"""
d={}  ## Empty Dictionary
d1=dict()   ## Empty Dictionary 
print(d,d1)
d={100:'Vignesh',200:"Priya",300:'Privika'}
print(d)
lst=[(1,30),(2,40),(3,50)]
d1=dict(lst)       ## Each tuple element consider as key and value pair.
print(d1)

dynamic_d=eval(input("Enter Dictionary:"))      ## give input    {1:'a',2:'b',3:'c'}
print(dynamic_d)


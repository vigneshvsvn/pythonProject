"""
1. List Merging
	- Way 1 Using + Operator
	- Way 2 l4=[*l1,*l2]  --> *l1 means all values of l1    - using * called  Keyword Arguments
2. Tuple Merge
	- Way 1 Using + operator
	- way 2 t4=(*t1,*t2)
3. Set Merge
	+ operators not allowed for set as order is not there.
	we need to use s3={*s1,*s2} only
4. Dict Merging
	+ not allowed
	 d3={**d1,**d2}    Note: two star we need to use as Key and Value


"""
## list Merge
l1=[1,2]
l2=[3,4]
l3=l1+l2
print(l3)
l4=[*l1,*l2]
print(l4)


####Tuple Merging
t1=(1,2)
t2=(3,4)
t3=t1+t2
print(t3)
t4=(*t1,*t2)
print(t4)

### Set Merging
s1={1,2}
s2={3,4}
s3={*s1,*s2}
print(s3)

### Dict Merge
d1={1:'a',2:'b'}
d2={3:'c',4:'d'}
d3={**d1,**d2}
print(d3)







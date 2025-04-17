""""
1.Empty Set Object --> s=set()
2. If we know data already s1={10,20,30,40,50}
3. using set() --> set(list/tuple...sequence, range)


"""

s=set() ## Empty set Object
print(type(s),s)
s1={10,20,30,40,50}
print(type(s1),s1)
s3=set(range(1,110,15))
print(type(s3),s3)
lst=[1,2,3,4,5,6,7]
s4=set(lst)
print(type(s4),s4)
s5=set("vignesh")     ## <class 'set'> {'h', 'e', 'n', 's', 'v', 'i', 'g'}  Order no guarantee 
print(type(s5),s5)

s6=eval(input("Enter values of set:"))
print(type(s6),s6)

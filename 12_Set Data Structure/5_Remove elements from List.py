"""
1. remove()    --> If value available in set then remove. If not available then through key error
2. discard()   --> If available it will remove or else it's ignore don't do anything
3. pop()       --> To Remove random element. Note list should not be empty
4.clear()      -->  Clear all elements from the set 


"""
s1={1, 2, 3, 67, 34, 678, 33, 12, 45, 44, 50, 22}
print(s1)
s1.remove(33)
print(s1)
if 100 in s1:
	s1.remove(100)       ## KeyError: 100  as 100 is not available in set. So always check element available in the set before removing it.
print(s1)

s1.discard(44)
s1.discard(101)        ## No error even it not available
print(s1)
p1=s1.pop()            ## Random element will be removed
print(s1,p1)               ## p1 is the element removed from the set

s1.clear()
print(s1)




"""
List Comprehension : To Create list with very easy way.
					 - Concise/Easy way of list creation
syntax:   lst= ['expression' (for 'each_element' in 'sequence') if (condition)]

"""
# lst=[1,2,3,4,5,6,7,8,9,10]
# ## normal way
# l=[]
# for i in range(1,11):
# 	l.append(i)
# print("l:",l)

### Using Comprehension
l1=[x for x in range(1,11)]
print("l1:",l1)
### To Create list of square number from 1-10 
l2= [x**2 for x in range(1,11)]
print("l2:",l2)
####
l3=[ x for x in range(1,101) if x%10 ==0]
print("l3:",l3)







from random import *

##help(random)

print(random())      			## Generate  random float number between   0 to 1
print(uniform(1,10))     ## Generate random float Number between begin and end. Boundary is fixed.
print(randint(1,6))      ## Generate random value inclusive start and end
print(randrange(1,10,1))     ## Start to stop -1 : Start and Step is optional. Start Default is 0 and step default is 1. stop is mandatory



otp=[str(randint(0,9)) for each in range(1,7)]      ## 6 digit random otp
print(str(otp))
print("Your Otp is:", ''.join(otp))

list=[10,20,30,40,50,60]
aphahabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

print(choice(aphahabets))
print(choice(list))       ## parameter should be indexable sequence list,string,tuple
print(choice(aphahabets)) ## random alpha

for i in range(11):
	otp = [str(randint(0, 9)) for each in range(1, 7)]
	print(f"Your Otp {i} is:", ''.join(otp))

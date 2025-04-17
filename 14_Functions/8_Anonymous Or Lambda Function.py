"""
Anonymous FUnction: Name less function. it's also call Lambda functions.

- It's used for instance use(one time usage) and never going to use multiple times.
  So name is not required as we are going to use only one time.

lambda input_args : expression
Eg: Square number
lambda n: n*n


"""

s=lambda n: n*n                  ## this is not the proper way of
print(s(4))
sum=lambda a,b:a+b               ## sample for two variable
print("sum:",sum(10,20))

bignumber=lambda a,b,c : a if a >b and a>c else b if  b >c  else c      ## using ternary expression       a if a >b and a>c else b if  b >c  else c

print(bignumber(10,320,34))





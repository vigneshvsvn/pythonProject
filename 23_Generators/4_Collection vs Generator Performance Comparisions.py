import time
from random import *

names=['Sunny','Bunny','Chinny','Vinny']
subjects=['Python','Java','DataScience']

def student_list(num):
	students=[]
	for i in range(num):
		student={
			'id': 1,
			'name':choice(names),
			'subject':choice(subjects)
					}
		students.append(student)
	return students

def studentGenerator(num):
	for i in range(num):
		student = {
			'id' : 1,
			'name' :choice(names),
			'subject' : choice(subjects)
		}
		yield student

t1=time.perf_counter()
print(t1)
s=student_list(10000)
time.sleep(1)
t2=time.perf_counter()
print(t2)
print("Time required to Create Student Object using Collection:",t2-t1)

t3=time.perf_counter()
print(t3)
g=studentGenerator(10000)
t4=time.perf_counter()
print(t4)
print("Time required to Create Student Object using Generator:",t4-t3)



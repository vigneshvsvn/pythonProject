students={
	"Vicky":['linux','sql','python','devops'] ,
	"venkat":['java','.net','spring','sprintboot']
}

for key in students.keys():
	print(key,':')
	for cources in students[key]:
		print(cources)
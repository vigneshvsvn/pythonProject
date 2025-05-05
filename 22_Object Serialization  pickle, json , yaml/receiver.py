import pickle

f=open('emp.ser','rb')
print("Deserialize emp object and printing.")
while True:
	try:
		e=pickle.load(f)
		print(e)
		print("*"*35)

	except EOFError:
		break

print("Deserialization of all employee Objectes Completed. ")


	
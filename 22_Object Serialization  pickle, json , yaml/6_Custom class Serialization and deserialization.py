"""
Directly it's not possible using dump(),dumps() and load (), loads() as these works only for dict objects.

If we want, we need to write extra code.

Serialization custom class:
emp object --> Dict object --> Json 

Deserialization:
json --> dict --> emp Object

"""
import json


import emp

## Serialization

e=emp.Employee(1,'Vignesh',10000.0,'Bangalore')
e_dict={
	'eNum':e.empNumber,
	'eName':e.empName ,
	'eSal':e.empSalary,
	'eCity':e.empCity
	
}
e_dict1=e.__dict__      ## using __dict__ variable converted to dict
print("Manual Dict Conversion:",e_dict)
print("\nManual Dict Convention using __dict__:",e_dict1)

json_string=json.dumps(e_dict1,indent=4)
print("\nJson String:",json_string)

## Deserialization

dict_deserial=json.loads(json_string)
print(dict_deserial)

emp1=emp.Employee(dict_deserial['empNumber'],dict_deserial['empName'],dict_deserial['empSalary'],dict_deserial['empCity'])

print(emp1)



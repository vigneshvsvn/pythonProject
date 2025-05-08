""""
To serialization/deserialize customized object

pip install jsonpickle

module: jsonpickle
encode() --> customized Object to Json
decode() --> json to customized object


"""
import emp,jsonpickle


e=emp.Employee(1,'Vignesh',10000.0,'Bangalore')
## Serialize to string
json_string=jsonpickle.encode(e)
print(json_string)
## if want to write to fine we need to take care
with open('emp1.json','w') as f:
	f.write(json_string)


## Deserialization
emp_object=jsonpickle.decode(json_string)
emp_object.display()

## Deserialization from File
with open('emp1.json','r') as f:
	json_str2=f.readlines()[0]

print(json_str2)

emp_obj2=jsonpickle.decode(json_str2)
emp_obj2.display()


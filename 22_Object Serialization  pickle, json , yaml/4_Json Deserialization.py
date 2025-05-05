import json
from json import loads

json_string="""
{
    "name": "Vignesh",
    "age": 33,
    "salary": 10000.0,
    "isMarried": true,
    "isHavingGirlFriend": null
}"""
print("Json String:",json_string)

#### Deserialize from Json String
employee=json.loads(json_string)        ## Json string to dict
print(type(employee),'**********')
print('Dict after Deserialization json string')
for k,v in employee.items():
	print(k,':',v,sep='')


########Deserialize from Json File
with open('emp.json','r') as f:
	employee1=json.load(f)
print('********Dict after Deserialization json File*********')
for k,v in employee1.items():
	print(k,':',v,sep='')




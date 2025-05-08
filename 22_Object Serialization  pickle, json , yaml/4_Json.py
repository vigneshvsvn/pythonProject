"""
Inter Operability:  Webservice, RESTAPI
	- How different applications will communicate each other.
	- common message format xml/json/yaml
		json --> light weight required less storage and easy to read.
		yaml --> light weight
		xml --> Heavy Weight
	- converting python data to Json called serialization.
	- convertion json to a python object called DeSerialization

json: Javascript object Notation.
	- Group of Key value Pair.

use json module.
	- serialization :  python object(dict) to json.
			dump() -->  dict to json file
			dumps() --> dict to json string
	- Deserialization: json to dict
			load() -->   json file to dict object
			loads() -->  json string to dict object
"""

import json
from json import dumps

employee={
	'name':'Vignesh',
	'age':33,
	'salary':10000.0,
	'isMarried':True,
	'isHavingGirlFriend':False
}

## Serialize python object to json String
json_string=json.dumps(employee,indent=4,sort_keys=True)
print('Python Dict:',employee)
print('Json String:',json_string)

with open('emp.json','w') as f:
	json.dump(employee,f,indent=4)

print("Json file Created, Please open 'emp.json' file and verify.")




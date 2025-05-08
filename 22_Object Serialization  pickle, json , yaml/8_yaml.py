""""
YAML --> Yaml Ain't Markup language  or Yet Another Markup Language

Advanced to Jason
 - Yaml more lightweight compared to  json.
 - more readable that json
 library: pyaml
 - pip install pyaml
 pyaml library contains Module: yaml
  contains:
 For Serialization dump() --> python dict object to yaml string or yaml file
 For Deserialization load() --> yaml string or yaml file to python dict
					safe_load() --> Recommended to use as load() is deprecated.
"""
from pyaml import yaml

emp_dict={
    "name": "Vignesh",
    "age": 33,
    "salary": 10000.0,
    "isMarried": True,
    "isHavingGirlFriend": None,
	"isHavingCar": False
}

## Serialization
yaml_string=yaml.dump(emp_dict)
print(yaml_string)

## Deserialization

new_dict=yaml.safe_load(yaml_string)

print(new_dict)

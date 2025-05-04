
import csv
with open('emp.csv','r') as f:
	reader=csv.reader(f)
	print(type(reader))
	data=list(reader)     ## we get data as list of list
	print(data)
	for each_data in data:
		print(','.join(each_data))


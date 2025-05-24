"""
UserName: HR
password:Password1234

Hostname: localhost
port: 1521
SID: DISZP101

Ways to Connect database:
using tnsname: conn = cx_Oracle.connect("username", "password", "tns_alias")
using full connection string: conn = cx_Oracle.connect("username/password@host:port/service_name")
using Separate Parameter:
conn = cx_Oracle.connect(
    user="username",
    password="password",
    dsn="host:port/service_name"
)

"""

import oracledb

try:
	conn=oracledb.connect(
		user='HR',
		password='Password1234',
		dsn="localhost:1521/DISZP101"
		)
	if conn is not None:
		print(f"Connected to {conn.db_name} database Successfully with {conn.username} account.")
		print(f"Oracle Version:",conn.version)

	cur=conn.cursor()

## Create Table
	cur.execute('create table PYTEST_EMP(enum number,eame varchar(20),esal number(10,2),eaddr varchar(100))')
	print("Table Created successfully.")

# Drop the Table
	# cur.execute('drop table PYTEST_EMP')
	# print("Table Dropped successfully.")

except oracledb.DatabaseError as msg:
	print("There is some problem.", msg)
finally:
	if cur is not None :
		cur.close()
	if cur is not None :
		conn.close()
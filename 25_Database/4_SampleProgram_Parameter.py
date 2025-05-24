"""
cursor.executemany(sql_statement, list_of_tuples)
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

##
	query='insert into PYTEST_EMP values(:ENUM, :EAME, :ESAL, :EADDR)'
	data=[(1,'Vignesh',10000,'Bangalore'),(2,'Priya',10000,'Bangalore'),(3,'Privika',10000,'Bangalore'),(4,'Amma',10000,'Bangalore'),(5,'Ayya',10000,'Bangalore')]
	cur.executemany(query,data)
	conn.commit()
	print("Rows Inserted successfully.")


except oracledb.DatabaseError as msg:
	print("There is some problem.", msg)
	conn.rollback()
finally:
	if cur is not None :
		cur.close()
	if cur is not None :
		conn.close()
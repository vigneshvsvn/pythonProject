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

## Insert Single Row
	cur.execute("insert into PYTEST_EMP values(1,'Vignesh',10000,'Bangalore')")
	conn.commit()
	print("Row Inserted successfully.")

except oracledb.DatabaseError as msg:
	print("There is some problem.", msg)
	conn.rollback()
finally:
	if cur is not None :
		cur.close()
	if cur is not None :
		conn.close()
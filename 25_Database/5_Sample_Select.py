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

## Select
	query='select * from PYTEST_EMP'
	cur.execute(query)
	row=cur.fetchone()
	while row is not None:
		print(row)
		row=cur.fetchone()

except oracledb.DatabaseError as msg:
	print("There is some problem.", msg)

finally:
	if cur is not None :
		cur.close()
	if cur is not None :
		conn.close()
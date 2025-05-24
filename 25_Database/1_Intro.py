"""
1. Temp Storage  : list, tuple ,dict, set ....
2. Permanent Storage: File, Database, Hadop...
Files: provided by local OS, used to store small amount of data
Database: 
persistent means  permanent


Module: cx_Oracle used to communicate to oracle database
Module: pymssql	 used to communicate to SQL server
Module : pymysql used to communicate to MYSQL database server.
pip install cx_Oracle --> Old but sill in use for old codes
pip install oracledb --> Latest module

1. import database module

2. Connect with a database, we need connection Object
connection=cx_Oracle.connect(database connection string)

3. Execute query and Hold result data: We need Cursor Object
cursor=conn.cursor()

4. By using a cursor object, we can execute SQL Queries.
execute(sqlQuery) --> One SQL statement
executescript(SQL Queries) --> group of SQL statement separated by ;
executemany() --> To  Execute a Parameterized query (Prepared statement in Java)

5. For DML: commit or rollback
commit()
rollback()

6. To Read the data from a select statement.
fetchone() --> one row
fetchall() --> all rows into a list
fetchmany(n) --> To fetch first n rows

7. Close the connection and Close Cursor in reverse order of Opening
cursor.close()
conn.close()

"""


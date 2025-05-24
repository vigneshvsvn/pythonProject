""""
Good Programming practices:

Synchronization:
Lock:
	l.acquire()
		execute a critical section of code required synchronization.   --> write in try block and write exception 
	l.release()  -->highly recommended to release in finally block

 	highly recommended us with statement, as it's take care of release automatically, so we no need of try,except and finally
 	with lockObject:
 		execute the code




"""
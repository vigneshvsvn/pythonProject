"""
1. logging.basicConfig() will take always first config.
	Both basicConfig can't be used at the same time.
2. It's not possible to config logger with different level with different configurations.
3. We can't specify multiple log files for different modules

If we depend on root loger above are the problems. To Overcome above issues we need to go for Custom Logger.

"""

import logging

logging.basicConfig(filemode='a',
					filename='log.txt',
					level=logging.INFO,
					format='%(asctime)s:%(levelname)s:%(processName)s:%(message)s',
					datefmt='%Y%m%d %H:%M:%S')

logging.basicConfig()
logging.info("A new request Came and started processing...")
try:
	x=int(input('Enter First Number:'))
	y=int(input('Enter Second Number:'))
	print('The Result:',x/y)
except ZeroDivisionError as msg:
	print("Can't Divide by Zero.")
	logging.exception(msg)

except ValueError as msg:
	print("Provide only Int type data.")
	logging.exception(msg)

logging.info("A request processing Completed.")
import logging

logging.basicConfig(filemode='a',
					filename='log.txt',
					level=logging.INFO,
					format='%(asctime)s:%(levelname)s:%(processName)s:%(message)s',
					datefmt='%Y%m%d %H:%M:%S')
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
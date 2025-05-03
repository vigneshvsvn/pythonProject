import logging
import Student
logger=logging.getLogger("vickylogger")
logger.setLevel(logging.DEBUG)

fileHandler=logging.FileHandler(filename='Program2.log',mode='a')
formatter=logging.Formatter('%(asctime)s:''%(levelname)s:'
							'%(process)d:'
							'%(message)s.',
							datefmt='%Y%m%d %H:%M:%S')
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)


logger.info("This is Info Message from Program 2.")
logger.warning("This is Warning Message  from Program 2.")
logger.error("This is an Error Message  from Program 2.")
logger.critical("This is a Critical message from Program 2.")
logger.debug("This is a Debug message from Program 2.")



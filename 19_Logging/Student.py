import logging
logger=logging.getLogger("Studentlogger")
logger.setLevel(logging.DEBUG)

fileHandler=logging.FileHandler(filename='Student.log',mode='a')
formatter=logging.Formatter('%(asctime)s:''%(levelname)s:'
							'%(process)d:'
							'%(message)s.',
							datefmt='%Y%m%d %H:%M:%S')
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)


logger.info("This is Info Message from Student.")
logger.warning("This is Warning Message  from Student.")
logger.error("This is an Error Message  from Student.")
logger.critical("This is a Critical message from Student.")
logger.debug("This is a Debug message from Student.")


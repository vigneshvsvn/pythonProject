import logging
logger=logging.getLogger("vickylogger")
logger.setLevel(logging.DEBUG)
consoleHandler=logging.StreamHandler()
consoleHandler.setLevel(logging.ERROR)
fileHandler=logging.FileHandler(filename='Program2.log',mode='a')

formatter=logging.Formatter('%(asctime)s:''%(levelname)s:'
							'%(process)d:'
							'%(message)s.',
							datefmt='%Y%m%d %H:%M:%S')
consoleHandler.setFormatter(formatter)
fileHandler.setFormatter(formatter)
logger.addHandler(consoleHandler)
logger.addHandler(fileHandler)


logger.info("This is Info Message.")
logger.warning("This is Warning Message.")
logger.error("This is an Error Message.")
logger.critical("This is a Critical message.")
logger.debug("This is a Debug message.")



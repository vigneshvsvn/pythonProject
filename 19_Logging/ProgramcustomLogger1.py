import logging

#Step 1: Create logger Object and set Level
logger=logging.getLogger('gvkLogger')
logger.setLevel(logging.INFO)
#Step 2: Create handler Object and set Level. Now want to use Console Handler
fileHandler=logging.FileHandler("Abc.log",mode='w')     # File Handler Sample
fileHandler.setLevel(logging.ERROR)
#Step 3: Create Formatter Object.
formatter=logging.Formatter('%(asctime)s:%(levelname)s:%(processName)s:%(message)s',
							datefmt='%Y%m%d %H:%M:%S')
#Step4: Set Formatter to Handler
fileHandler.setFormatter(formatter)
#Step 5: add Handler to logger
logger.addHandler(fileHandler)
logger.info("This is Info Message.")
logger.warning("This is Warning Message.")
logger.error("This is an Error Message.")
logger.critical("This is a Critical message.")

"""
We need to create 3 Objects
1. Logger object --> To implement our custom logger.
2. Handler Object --> How to handle, display to Console, log to file, or by email ..... We have multiple Handlers
					To display in Console: StreamHandler
					To the File: FileHandler
					BY Email: SMTPHandler
					To Webserver:HTTPHandler
3. Formatter Object --> Responsible to format the Message.
"""
import logging
from xml.sax import ContentHandler

#Step 1: Create logger Object and set Level
logger=logging.getLogger('gvkLogger')
logger.setLevel(logging.INFO)

#Step 2: Create handler Object and set Level. Now want to use Console Handler
consoleHandler=logging.StreamHandler()
consoleHandler.setLevel(logging.ERROR)
# fileHandler=logging.FileHandler("Abc.log",mode='w')     # File Handler Sample
# fileHandler.setLevel(logging.ERROR)

#Step 3: Create Formatter Object.
formatter=logging.Formatter('%(asctime)s:%(levelname)s:%(processName)s:%(message)s',
							datefmt='%Y%m%d %H:%M:%S')
#Step4: Set Formatter to Handler
consoleHandler.setFormatter(formatter)

#Step 5: add Handler to logger
logger.addHandler(consoleHandler)

# step 6: Write log message by Loger Object
logger.info("This is Info Message.")
logger.warning("This is Warning Message.")
logger.error("This is an Error Message.")
logger.critical("This is a Critical message.")


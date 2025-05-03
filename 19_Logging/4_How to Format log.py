"""
Default Format: level name:logger name : message
Example:
	CRITICAL:root:This is Critical.
	ERROR:root:This is an Error Message.
	WARNING:root:This is a Warning.

Syntax: format='%()s'
format='%(levelname)s'

format='%(asctime)s:%(levelname)s:%(message)s:%(name)s'


"""

import logging
from fileinput import filename

logging.basicConfig(filemode='a',filename='log.txt',level=30,format='%(asctime)s:%(levelname)s:%(message)s')
logging.critical("This is Critical.")
logging.error("This is an Error Message.")
logging.warning("This is a Warning.")
logging.info("This is Info Message.")
logging.debug("This is Debug info.")

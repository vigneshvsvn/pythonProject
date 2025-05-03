"""
filemode='w' --> Overwrite
filemode='a' --> Append is by Default

level='30' --> Warning is the Default

if filename is not specified, then it will write to the Console not to any log file.

"""

import logging

#logging.basicConfig(filename='log.txt',level=logging.WARNING,filemode='w')
logging.basicConfig(filename='log.txt')
#logging.basicConfig()
logging.critical("This is Critical.")
logging.error("This is Error Message.")
logging.warning("This is a Warning.")
logging.info("This is Info Message.")
logging.debug("This is Debug info.")

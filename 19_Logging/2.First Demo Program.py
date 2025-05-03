"""

Basic Requirement:
1. one file is required to write logging.
2. which level of data needs to write?

logging.basicConfig(filename='log.txt',level=logging.WARNING)   --> Upto this level it will write.
			Eg: warning means Critical,Error amd warning are allowed. Up to this level it will allow to write.
logging.critical(message)
logging.error(message)
logging.warning(message)
logging.info(message)
logging.debug(message)

"""
import logging

logging.basicConfig(filename='log.txt',level=logging.WARNING)
logging.critical("This is Critical.")
logging.error("This is Error Message.")
logging.warning("This is Warning.")
logging.info("This is Info Message.")
logging.debug("This is Debug info.")



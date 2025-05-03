"""

"""

import logging
from fileinput import filename

logging.basicConfig(filemode='w',filename='log.txt',level=30,format='%(asctime)s:%(levelname)s:%(message)s',
					datefmt='%Y%m%d %H:%M:%S')
logging.critical("This is Critical.")
logging.error("This is an Error Message.")
logging.warning("This is a Warning.")
logging.info("This is Info Message.")
logging.debug("This is Debug info.")

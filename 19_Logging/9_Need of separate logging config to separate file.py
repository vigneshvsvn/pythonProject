"""
need of Separating Logger Config into a separate file or dict or Json of Yaml .

Why ?
- All logging config in each module. Then changing is logging is complex.
- For Code Reusability
- length of code will reduce so readability will increase.

From the config file we will load and use in our applications.

logging_config.properties --> Any name and any extension can be used.

"""


import logging.config
logging.config.fileConfig('logging_config.properties')
logger=logging.getLogger('demologger')

logger.info("This is Info Message.")
logger.warning("This is Warning Message.")
logger.error("This is an Error Message.")
logger.debug("This is a Debug Message.")
logger.critical("This is a Critical Message.")


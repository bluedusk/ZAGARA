
import logging
import os
import sys
sys.path.append("..")
from zagara.logger import Logger

print os.getcwd()
#logging.basicConfig(filename = os.path.join(os.getcwd(), 'debug.log'), format = '[%(levelname)s] - %(asctime)s - %(message)s', level = logging.DEBUG)
#logging.debug('this is a message')


logger = Logger().getlog()
logger.debug("what the fuck");
logger.info('info msg')  
logger.debug('debug msg') 
#logger.warning("what the fuck");

import logging
logging.basicConfig(level=logging.INFO ,format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)  

lf=logging.FileHandler('anivlogfile2.log')
formatter    = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
lf.setFormatter(formatter)

# add file handler to logger
logger.addHandler(lf)
def getemi():
    logger.info('function started')
    print('emi amount is 9999')
    logger.info('function end')
logger.info('function called 1st time')
getemi()
logger.info('funciton called 2nd time')
getemi()
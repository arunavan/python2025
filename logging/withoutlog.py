import logging

# Configure logging
logging.basicConfig(level=logging.INFO ,format='%(asctime)s - %(levelname)s - %(message)s')

# Example usage
def calculate_sum(a, b):
    result = a + b
    return result

logger = logging.getLogger(__name__)  

lf=logging.FileHandler('anivlogfile4.log')
formatter    = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
lf.setFormatter(formatter)

# add file handler to logger
logger.addHandler(lf)

logger.info("started")
result = calculate_sum(10, 20)
print(result)
logger.info("stoped")

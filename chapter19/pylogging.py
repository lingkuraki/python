import logging

logging.basicConfig(level=logging.INFO, filename='mylog.log')
logging.info('项目开始')
logging.info('Trying to divide 1 by 0')
print(1 / 0)
logging.info('The division succeeded')
logging.info('Ending program')

import logging

# print a log message to the console
#logging.warning('This is a warning')

#logging.basicConfig(filename='program.log',level=logging.DEBUG)
#logging.warning('An example message')
#logging.error('Another error message')

# Time in log
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
logging.info('Logging app started')
logging.warning('An example logging message')
logging.warning('Another time log')
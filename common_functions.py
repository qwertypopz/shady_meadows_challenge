from webdriverwrapper import Firefox
import logging

def setup_driver(log):
    driver = Firefox()
    log.info('Driver instantiated!')
    return driver

def setup_logger():
    log = logging.getLogger('log')
    log.info('Log function has been added')
    return log


from webdriverwrapper import Firefox
import logging

def navigate_to_main(driver, logger):
    logger.info('Navigating to main page')
    driver.get('https://automationintesting.online/#/')

def setup_driver(log):
    '''
    Sets up a driver engine that will allow online navigation through a Firefox browser
    :param log: Utilized for testing and diagnostics
    :return: Returns a driver object for use
    '''
    driver = Firefox()
    log.info('Driver instantiated!')
    return driver

def setup_logger():
    '''
    Sets up logging functionality for testing and diagnostic purposes
    NOTE: print
    :return: Returns a logger object for use
    '''
    log = logging.getLogger('log')
    log.info('Log function has been added')
    return log


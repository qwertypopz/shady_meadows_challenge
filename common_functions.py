'''
Collection of common functions
author: Tommy Nguyen
date: 2019.10.04
'''
from webdriverwrapper import Firefox

import datetime
import logging

def admin_login(driver, log):
    '''
    Log in as administrator
    :param driver: Allows use of browser
    :param log: For testing and diagnostics
    :return:
    '''
    log.info("Navigating to admin panel")
    driver.get("https://automationintesting.online/#/admin")
    try:
        driver.get_elm(css_selector='#username').send_keys('admin')
        driver.get_elm(css_selector='#password').send_keys('password')
        driver.get_elm(css_selector='#doLogin').click()
    except:
        pass

def navigate_calendar(start_date, driver, log):
    '''
    Navigates to the correct calendar month to reserve room
    :param start_date: datetime variable stating reservation start date Can be defined by datetime.datetime(YYYY, MM, DD)
    :param driver: Allows user of web browser
    :param log: For testing and diagnostics
    :return:
    '''
    log.info("Navigating to the correct calendar month")
    calendar = driver.find_element_by_text(datetime.datetime.now().strftime("%B %Y"))
    calendar_start = start_date.strftime("%B %Y")
    if start_date > datetime.datetime.now():
        button_text = 'Next'
    else:
        button_text = 'Back'
    while calendar.text != calendar_start:
        driver.get_elm(text=button_text).click()

def navigate_to_main(driver, log):
    '''
    Navigates to the main page
    :param driver: Allows use of web browser
    :param log: For testing and diagnostics
    :return:
    '''
    log.info('Navigating to main page')
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

def setup_log():
    '''
    Sets up logging functionality for testing and diagnostic purposes
    NOTE: print
    :return: Returns a logger object for use
    '''
    log = logging.getLogger('log')
    log.info('Log function has been added')
    return log

def skip_splash(driver, log):
    '''
    Skips the splash page
    :param driver: Allows use of web browser
    :param log: For testing and diagnostics
    :return: None
    '''
    log.info("Skipping splash screen")
    while driver.get_elm(xpath='/html/body/div/div[1]/div[2]/div/div').is_displayed():
        try:
            driver.get_elm(xpath='//*[@id="next"]').click()
        except:
            driver.get_elm(xpath='//*[@id="closeModal"]').click()
            #Utilizing break due to while condition being poorly defined. Will always be true
            break

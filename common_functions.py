from time import sleep
from selenium.webdriver import ActionChains
from webdriverwrapper import Firefox

import datetime
import logging

def make_reservation(room, date_start, duration, driver, log):

    input_first = "Tommy"
    input_last = "Nguyen"
    input_email = "tommy.nguyen@fakelook.com"
    input_phone = "703-801-9999"

    navigate_to_main(driver, log)
    skip_splash(driver, log)

    #Start Booking Process
    log.info("Start booking process for a " + room)
    driver.get_elm(xpath='//*[contains(text(), "' + room + '")]/../button').click()

    #Find the calendar with the start date
    calendar = driver.find_element_by_text(datetime.datetime.now().strftime("%B %Y"))
    calendar_start = date_start.strftime("%B %Y")
    if date_start > datetime.datetime.now():
        button_text = 'Next'
    else:
        button_text = 'Back'
    while calendar.text != calendar_start:
        driver.get_elm(text=button_text).click()

    #Do that drag and drop thing
    day_start = date_start.strftime("%d")
    date_end = date_start + datetime.timedelta(days=duration)
    day_end = date_end.strftime("%d")
    if day_start > day_end:
        class_attribute = "rbc-off-range"
    else:
        class_attribute = "rbc-day-bg"
    drag_start = driver.get_elm(xpath='//a[contains(text(), "' + day_start +
                                      '")]/ancestor::div[//div[@class="rbc-day-bg"] and @class="rbc-date-cell"]')
    drag_end = driver.get_elm(xpath='//a[contains(text(), "' + day_end + '")]/ancestor::div[//div[@class="' +
                                    class_attribute + '"] and @class="rbc-date-cell"]')
    ac = ActionChains(driver)
    ac.drag_and_drop(drag_start, drag_end).perform()
    sleep(5)

    #Complete booking form
    log.info("Filling out booking information")
    field_first = driver.get_elm(css_selector = '.room-firstname')
    log.info("Filling out Firstname field: " + input_first)
    field_first.send_keys(input_first)
    field_last = driver.get_elm(css_selector = '.room-lastname')
    log.info("Filling out Lastname field: " + input_last)
    field_last.send_keys(input_last)
    field_email = driver.get_elm(css_selector = '.room-email')
    log.info("Filling out Email field: " + input_email)
    field_email.send_keys(input_email)
    field_phone = driver.get_elm(css_selector = '.room-phone')
    log.info("Filling out Phone field: " + input_phone)
    field_phone.send_keys(input_phone)

    driver.get_elm(text="Book").click()
    '''
    '//div[@class="rbc-day-bg" and //a[contains(text(),"05")]]'
    '//a[contains(text(), "05")]/ancestor::div[@class="rbc-day-bg"]'
    '''


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

def setup_logger():
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
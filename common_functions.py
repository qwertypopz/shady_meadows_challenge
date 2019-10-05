'''
Collection of common functions
author: Tommy Nguyen
date: 2019.10.04
'''
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
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

def make_reservation(room, start_date, duration, driver, log):
    '''
    Navigates to the main page, skips the splash screen, and creates a reservation under the specified room for a test
    customer
    :param room: String variable denoting type of reservation ['Single', 'Double', 'Family', 'Suite']
    :param start_date: datetime variable stating reservation start date Can be defined by datetime.datetime(YYYY, MM, DD)
    :param duration: integer variable stating duration of reservation in days
    :param driver: Allows use of browser
    :param log: For testing and diagnostics
    :return: Boolean value declaring success (True) or failure (False)
    '''
    input_first = "Automation"
    input_last = "Test"
    input_email = "automation.test@fakelook.com"
    input_phone = "703-888-9999"

    navigate_to_main(driver, log)
    skip_splash(driver, log)

    #Start Booking Process
    log.info("Start booking process for a " + room)
    reservation = driver.get_elm(xpath='//*[contains(text(), "' + room + '")]/../button')
    driver.execute_script("return arguments[0].scrollIntoView();", reservation)
    reservation.click()

    navigate_calendar(start_date, driver, log)

    #Do that drag and drop thing
    start_day = start_date.strftime("%d")
    if datetime.datetime.now().strftime("%Y-%m-%d") == start_date.strftime("%Y-%m-%d"):
        start_class_attribute = '"rbc-date-cell rbc-now rbc-current"'
    elif start_day == datetime.datetime.now().strftime("%d"):
        start_class_attribute = '"rbc-date-cell rbc-current"'
    else:
        start_class_attribute = '"rbc-date-cell"'
    end_date = start_date + datetime.timedelta(days=duration)
    end_day = end_date.strftime("%d")

    if start_date.strftime("%m") == end_date.strftime("%m"):
        end_class_attribute = '"rbc-date-cell"'
    else:
        end_class_attribute = '"rbc-date-cell rbc-off-range"'
    log.info("Setting reservation range")
    drag_start = driver.get_elm(xpath='//a[contains(text(), "' + start_day + '")]/..[@class=' +
                                      start_class_attribute + ']')
    drag_end = driver.get_elm(xpath='//a[contains(text(), "' + end_day + '")]/..[@class=' +
                                    end_class_attribute + ']')
    ac = ActionChains(driver)
    ac.drag_and_drop(drag_start, drag_end).perform()

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

    driver.get_elm(xpath='//*[@name="phone"]/../../button[contains(text(), "Book")]').click()

    # Occassionally fails the first attempt. Possibly due to network/browser issues. Look at wait_for_element()
    try:
        success = driver.get_elm(xpath='//h3[contains(text(),"Booking Successful!")]').is_displayed()
    except Exception as error:
        log.info("Failed to get success message. Trying again")
        sleep(3)
        success = driver.get_elm(xpath='//h3[contains(text(),"Booking Successful!")]').is_displayed()
    if success:
        log.info("Reservation form has been booked")
    return success

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

def verify_reservation_via_rooms(room, start_date, driver, log):
    '''
    Searches for reservation based on date for the room specified to validate reservation. This code was changed on
    2019.10.04 as the website changed without warning. Good times.
    Note: Sleep was used many times over as webdriverwrapper's wait_for_element function would not work. Need to be
    revisited
    :param room: String variable denoting type of reservation ['Single', 'Double', 'Family', 'Suite']
    :param date_start: datetime variable stating reservation start date Can be defined by datetime.datetime(YYYY, MM, DD)
    :param driver: Allows use of browser
    :param log: For testing and diagnostics
    :return: Boolean value declaring success (True) or failure (False)
    '''
    log.info("Verification through Rooms tab in Admin Panel")
    ids = {
        "Twin":"room1",
        "Single":"room2"
        #"Family":"room3",
        #"Suite":"room4"
    }
    costs = {
        "Single":19,
        "Double":149,
        "Family":349,
        "Suite":500
    }
    admin_login(driver, log)
    try:
        driver.get_elm(text="Rooms").click()
    except:
        sleep(3)
        driver.get_elm(text="Rooms").click()

    try:
        room_num = driver.get_elm(xpath='//*[@id="' + ids.get(room) + '"]')
    except:
        sleep(3)
        room_num = driver.get_elm(xpath='//*[@id="' + ids.get(room) + '"]')
    room_num.click()

    try:
        driver.get_elm(xpath='//*[contains(text(), "' + start_date.strftime("%Y-%m-%d") + '")]')
    except:
        sleep(3)
        driver.get_elm(xpath='//*[contains(text(), "' + start_date.strftime("%Y-%m-%d") + '")]')

    reservation = driver.get_elm(xpath='//*[contains(text(), "' + start_date.strftime("%Y-%m-%d") + '")]')
    if reservation.is_displayed():
        log.info("Reservation has been validated")
    return reservation.is_displayed()
'''
Make reservations
'''
import common_functions
import datetime
import sys

from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
def action(args, log):
    '''
    Navigates to the main page, skips the splash screen, and creates a reservation under the specified room for a test
    customer.
    :param args: This is a dictionary variable with the following key value pairs:
        :param room: String variable denoting type of reservation ['Single', 'Double', 'Family', 'Suite']
        :param start_date: datetime variable stating reservation start date Can be defined by
        datetime.datetime(YYYY, MM, DD)
        :param duration: integer variable stating duration of reservation in days
    :param log: For testing and diagnostics
    :return: Boolean value declaring success (True) or failure (False)
    '''
    log.info("Initiating reservation process")

    reservation_args = args
    room = reservation_args.get("room")
    start_date = reservation_args.get("start_date")
    duration = reservation_args.get("duration")
    input_first = "Automation"
    input_last = "Test"
    input_email = "automation.test@fakelook.com"
    input_phone = "703-888-9999"

    driver = common_functions.setup_driver(log)

    common_functions.navigate_to_main(driver, log)
    common_functions.skip_splash(driver, log)

    #Start Booking Process
    log.info("Start booking process for a " + room)
    reservation = driver.get_elm(xpath='//*[contains(text(), "' + room + '")]/../button')
    driver.execute_script("return arguments[0].scrollIntoView();", reservation)
    reservation.click()

    common_functions.navigate_calendar(start_date, driver, log)

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
    driver.wait_for_element(xpath='//h3[contains(text(),"Booking Successful!")]')
    room_reserved = driver.get_elm(xpath='//h3[contains(text(),"Booking Successful!")]').is_displayed()
    if room_reserved:
        log.info("Reservation form has been booked")
    return validate_rooms(args, log, driver)

def validate_rooms(args, log, driver):
    '''
    Searches for reservation based on date for the room specified to validate reservation. This code was changed on
    2019.10.04 as the website changed without warning. Good times.
    Note: Sleep was used many times over as webdriverwrapper's wait_for_element function would not work. Need to be
    revisited
    :param args: This is a dictionary variable with the following key value pairs:
        :param room: String variable denoting type of reservation ['Single', 'Double', 'Family', 'Suite']
        :param start_date: datetime variable stating reservation start date Can be defined by
        datetime.datetime(YYYY, MM, DD)
        :param duration: integer variable stating duration of reservation in days
    :param log: For testing and diagnostics
    :param driver: Allows use of browser
    :return: Boolean value declaring success (True) or failure (False)
    '''
    log.info("Initiating validation of reservation")

    reservation_args = args
    room = reservation_args.get("room")
    start_date = reservation_args.get("start_date")
    duration = reservation_args.get("duration")
    ids = {
        "Twin":"room1",
        "Single":"room2"
        #"Family":"room3",
        #"Suite":"room4"
    }
    common_functions.admin_login(driver, log)
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

if __name__ == '__main__':
    log = common_functions.setup_log()
    globals()[sys.argv[1]](log)

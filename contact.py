'''
Completes the contact section to get in touch with Sauce Labs
'''
import common_functions
import sys
from time import sleep
def action(log):
    '''
    Complete contact information found at the bottom of AiT homepage
    Note: wait_for_element doesn't function here. Given time, investigate further
    :param log: For testing and diagnostics
    :return: Boolean value declaring pass (True) or fail (False)
    '''
    log.info("Initiating contact form functionality test")

    args = {
        "input_name":"Automation Test",
        "input_email":"automation.test@fakelook.com",
        "input_phone":"703-888-9999",
        "input_subject":"Reservation Questions",
        "input_message":"This is a test email message"
    }

    driver = common_functions.setup_driver(log)
    common_functions.navigate_to_main(driver, log)
    common_functions.skip_splash(driver, log)
    field_name = driver.get_elm(css_selector='#name')
    log.info("Filling out Name field: " + args.get("input_name"))
    field_name.send_keys(args.get("input_name"))
    field_email = driver.get_elm(css_selector='#email')
    log.info("Filling out Email field: " + args.get("input_email"))
    field_email.send_keys(args.get("input_email"))
    field_phone = driver.get_elm(css_selector='#phone')
    log.info("Filling out Phone field: " + args.get("input_phone"))
    field_phone.send_keys(args.get("input_phone"))
    field_subject = driver.get_elm(css_selector='#subject')
    log.info("Filling out Subject field: " + args.get("input_subject"))
    field_subject.send_keys(args.get("input_subject"))
    field_message = driver.get_elm(css_selector='#description')
    log.info("Filling out Message field: " + args.get("input_message"))
    field_message.send_keys(args.get("input_message"))
    driver.get_elm(css_selector='#submitContact').click()
    try:
        confirmation = driver.find_element_by_text('Thanks for getting in touch')
    except:
        sleep(3)
        confirmation = driver.find_element_by_text('Thanks for getting in touch')
    if confirmation.is_displayed():
        log.info("Message sent")
        return validation(args, log, driver)

def validation(args, log, driver):
    '''
    Validates that the message was sent to the business.
    Note: wait_for_element doesn't function here. Given time, investigate further
    :param args: This is a dictionary variable with the following key value pairs:
        :param input_name: String value with name of user
        :param input_email: String value with email of user
        :param input_phone: String value with phone number of user
        :param input_subject: String value with subject of message
        :param input_message: String value with content of message
    :param log: For testing and diagnostics
    :param driver: Allows use of web browser
    :return: Boolean value declaring pass (True) or fail (False)
    '''
    log.info("Initiating validation of contact form test")

    input_name = args.get("input_name")
    input_email = args.get("input_email")
    input_phone = args.get("input_phone")
    input_subject = args.get("input_subject")
    input_message = args.get("input_message")

    common_functions.admin_login(driver, log)
    driver.get("https://automationintesting.online/#/admin/messages")
    try:
        message = driver.find_element_by_text(text=input_subject)
    except:
        sleep(3)
        message = driver.find_element_by_text(text=input_subject)
    message.click()
    sleep(3)
    try:
        check_name = driver.find_element_by_text(text=input_name).is_displayed()
        check_email = driver.find_element_by_text(text=input_email).is_displayed()
        check_phone = driver.find_element_by_text(text=input_phone).is_displayed()
        check_subject = driver.find_element_by_text(text=input_subject).is_displayed()
        check_message = driver.find_element_by_text(text=input_message).is_displayed()
    except:
        sleep(3)
        check_name = driver.find_element_by_text(text=input_name).is_displayed()
        check_email = driver.find_element_by_text(text=input_email).is_displayed()
        check_phone = driver.find_element_by_text(text=input_phone).is_displayed()
        check_subject = driver.find_element_by_text(text=input_subject).is_displayed()
        check_message = driver.find_element_by_text(text=input_message).is_displayed()
    if check_name and check_email and check_phone and check_subject and check_message:
        log.info("Validation complete")
    return check_name and check_email and check_phone and check_subject and check_message

if __name__ == '__main__':
    log = common_functions.setup_log()
    globals()[sys.argv[1]](log)
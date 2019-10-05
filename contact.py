'''
Completes the contact section to get in touch with Sauce Labs
'''
import common_functions
import sys

def fill_contact(log):
    '''
    Complete contact information found at the bottom of AiT homepage
    :param log: For testing and diagnostics
    :return: Boolean value declaring pass (True) or fail (False)
    '''

    input_name = "Automation Test"
    input_email = "automation.test@fakelook.com"
    input_phone = "703-888-9999"
    input_subject = "Reservation Questions"
    input_message = "This is a test email message"

    driver = common_functions.setup_driver(log)
    common_functions.navigate_to_main(driver, log)
    common_functions.skip_splash(driver, log)
    field_name = driver.get_elm(css_selector='#name')
    log.info("Filling out Name field: " + input_name)
    field_name.send_keys(input_name)
    field_email = driver.get_elm(css_selector='#email')
    log.info("Filling out Email field: " + input_email)
    field_email.send_keys(input_email)
    field_phone = driver.get_elm(css_selector='#phone')
    log.info("Filling out Phone field: " + input_phone)
    field_phone.send_keys(input_phone)
    field_subject = driver.get_elm(css_selector='#subject')
    log.info("Filling out Subject field: " + input_subject)
    field_subject.send_keys(input_subject)
    field_message = driver.get_elm(css_selector='#description')
    log.info("Filling out Message field: " + input_message)
    field_message.send_keys(input_message)
    driver.get_elm(css_selector='#submitContact').click()
    return driver.find_element_by_text('Thanks for getting in touch').is_displayed()

if __name__ == '__main__':
    log = common_functions.setup_log()
    globals()[sys.argv[1]](log)
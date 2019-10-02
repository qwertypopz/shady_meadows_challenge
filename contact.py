'''
Completes the contact section to get in touch with Sauce Labs
'''
import common_functions
import sys

def fill_contact(log):
    '''
    Complete contact information found at the bottom of AiT homepage
    :param logger: For testing and diagnostics
    :return: None
    '''
    driver = common_functions.setup_driver(log)
    common_functions.navigate_to_main(driver, log)
    common_functions.skip_splash(driver, log)
    name_field = driver.get_elm(xpath='//*[@id="name"]')
    name_field.send_keys('Tommy Nguyen')
    email = driver.get_elm(xpath='//*[@id="email')
    email.send_keys('nhatanguyen@outlook.com')
    phone = driver.get_elm(xpath='//*[@id="phone')
    phone.send_keys('703-801-4416')
    message = driver.get_elm(xpath='//*[@id="description')
    message.send_keys('This is a test email')
    #driver.get_elm(xpath='//*[@id="submitContact"]')
    driver.get_elm(css_selector='#submitContact')



if __name__ == '__main__':
    log = common_functions.setup_logger()
    globals()[sys.argv[1]](log)
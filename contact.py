import common_functions
import sys

def fill_contact(logger):
    '''
    Complete contact information found at the bottom of AiT homepage
    :param logger: For testing and diagnostics
    :return: None
    '''
    driver = common_functions.setup_driver(log)
    common_functions.navigate_to_main(driver, logger)
    name_field = driver.get_elm(xpath='//*[@id="name"]')
    name_field.send_keys('John')

if __name__ == '__main__':
    log = common_functions.setup_logger()
    globals()[sys.argv[1]](log)
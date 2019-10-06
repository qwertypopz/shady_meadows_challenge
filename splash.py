'''
This test checks the splash page of the AiT homepage.
TODO: The functions could be refactored to a simpler, reusable format
TODO: Consider checking the whole message if time allows
author: Tommy Nguyen
Date: 2019.10.01
'''
import common_functions
import sys

def splash_exists(driver, log):
    '''
    Make sure AiT homepage has a splash page
    :param logger: For testing and diagnostics
    :return: Boolean value declaring pass (True) or fail (False)
    '''
    common_functions.navigate_to_main(driver, log)
    #It's ugly but the element has no name or id
    splash = driver.get_elm(text="Welcome to Restful Booker Platform")
    return splash.is_displayed()

def page_1(driver, log):
    '''
    Checks first message of welcome splash
    :param log: For testing and diagnostics
    :return: Boolean value declaring pass (True) or fail (False)
    '''
    log.info("Validating Splash - Page 1")
    message_header = "Welcome to Restful Booker Platform"
    message = "Your one stop shop to practise Software Testing!"
    if driver.find_element_by_text(message_header).is_displayed():
        if driver.find_element_by_text(message).is_displayed():
            log.info("Validated")
            next = driver.get_elm(xpath='//*[@id="next"]')
            next.click()
            return True
    return False



def page_2(driver, log):
    '''
    Checks second message of welcome splash after checking preceding page
    :param log: For testing and diagnostics
    :return: Boolean value declaring pass (True) or fail (False)
    '''
    page_1(driver, log)
    log.info("Validating Splash - Page 2")
    message = "Testing is more than just finding bugs."
    if driver.find_element_by_text(message).is_displayed():
        log.info("Validated")
        next = driver.get_elm(xpath='//*[@id="next"]')
        next.click()
        return True
    return False


def page_3(driver, log):
    '''
    Checks third message of welcome splash after checking preceding pages
    :param log: For testing and diagnostics
    :return: Boolean value declaring pass (True) or fail (False)
    '''
    page_2(driver, log)
    log.info("Validating Splash - Page 3")
    message = "Restful-booker-platform is an open source"
    if driver.find_element_by_text(message).is_displayed():
        log.info("Validated")
        next = driver.get_elm(xpath='//*[@id="next"]')
        next.click()
        return True
    return False

def page_4(driver, log):
    '''
    Checks fourth message of welcome splash after checking preceding pages
    :param log: For testing and diagnostics
    :return: Boolean value declaring pass (True) or fail (False)
    '''
    page_3(driver, log)
    log.info("Validating Splash - Page 4")
    message = "Restful-booker-platform is a continuously"
    if driver.find_element_by_text(message).is_displayed():
        log.info("Validated")
        next = driver.get_elm(xpath='//*[@id="next"]')
        next.click()
        return True
    return False

def page_5(driver, log):
    '''
    Checks fifth message of welcome splash after checking preceding pages
    :param log: For testing and diagnostics
    :return: Boolean value declaring pass (True) or fail (False)
    '''
    page_4(driver, log)
    log.info("Validating Splash - Page 5")
    message = "How you use this application is up to you, but here"
    if driver.find_element_by_text(message).is_displayed():
        log.info("Validated")
        close = driver.get_elm(xpath='//*[@id="closeModal"]')
        close.click()
        driver.quit()
        return True
    return False


def validate(log):
    '''
    Checks that the splash page has the expected message
    :param log: For testing and diagnostics
    :return: Boolean value declaring pass (True) or fail (False)
    '''
    driver = common_functions.setup_driver(log)
    if splash_exists(driver, log):
        log.info("Splash exists. Validating message")
        if page_5(driver, log):
            return True
    return False

if __name__ == '__main__':
    log = common_functions.setup_log()
    globals()[sys.argv[1]](log)
'''
Make reservations
'''
import common_functions
import sys
import datetime

def action(log):
    '''
    Create a reservation for a Single room on a specified date and duration
    '''
    room = "Single"
    start_date = datetime.datetime.now()
    duration = 3

    driver = common_functions.setup_driver(log)
    common_functions.make_reservation(room, start_date, duration, driver, log)
    common_functions.verify_reservation_via_rooms(room, start_date, driver, log)
    driver.quit()

if __name__ == '__main__':
    log = common_functions.setup_log()
    globals()[sys.argv[1]](log)
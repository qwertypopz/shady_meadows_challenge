'''
Make reservations
'''
import common_functions
import contact
import reservation
import splash
import sys
import datetime


def splash_single_now_2(log):
    '''
    Validate splash page and then create a reservation for a Single room today for two days
    '''
    args = {
        "room":"Single",
        "start_date":datetime.datetime.now(),
        "duration":2
    }
    splash.validate(log)
    reservation.action(args, log)

def contact_twin_thanksgiving_3(log):
    '''
    Email the business through the contact form and then create a reservation for a Twin room for Thanksgiving for
    three days
    '''
    args = {
        "room":"Twin",
        "start_date":datetime.datetime(2019, 11, 27),
        "duration":3
    }
    contact.action(log)
    reservation.action(args, log)

if __name__ == '__main__':
    log = common_functions.setup_log()
    globals()[sys.argv[1]](log)
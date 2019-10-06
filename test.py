'''
Make reservations
'''
import common_functions
import reservation
import sys
import datetime

def single(log):
    '''
    Create a reservation for a Single room on a specified date and duration
    '''
    args = {
        "room":"Single",
        "start_date":datetime.datetime.now(),
        "duration":3
    }
    reservation.action(args, log)


if __name__ == '__main__':
    log = common_functions.setup_log()
    globals()[sys.argv[1]](log)
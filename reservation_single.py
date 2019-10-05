import common_functions
import sys
import datetime
from time import sleep

def test(log):
    start_date = datetime.datetime(2019, 10, 4)

    driver = common_functions.setup_driver(log)
    common_functions.make_reservation("Single", start_date, 3, driver, log)
    common_functions.verify_reservation_via_rooms("Single", start_date, driver, log)
    #common_functions.verify_reservation_via_report("Single", start_date, driver, log)

if __name__ == '__main__':
    log = common_functions.setup_logger()
    globals()[sys.argv[1]](log)
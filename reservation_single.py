import common_functions
import sys
import datetime
from time import sleep

def test(log):
    start_date = datetime.datetime(2019, 12, 1)

    driver = common_functions.setup_driver(log)
    common_functions.make_reservation("Single", start_date, 10, driver, log)
    sleep(10)
    driver.quit()

if __name__ == '__main__':
    log = common_functions.setup_logger()
    globals()[sys.argv[1]](log)
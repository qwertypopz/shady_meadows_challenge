import common_functions
import sys

if __name__ == '__main__':
    log = common_functions.setup_logger()
    globals()[sys.argv[1]](log)
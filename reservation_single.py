if __name__ == '__main__':
    log = setup_logger()
    globals()[sys.argv[1]](log)
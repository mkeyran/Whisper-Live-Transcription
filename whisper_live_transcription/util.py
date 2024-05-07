import logging

def setup_logger(module_name):
    logger = logging.getLogger(module_name)
    logger.setLevel(logging.INFO)
    # Write logs to console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    return logger
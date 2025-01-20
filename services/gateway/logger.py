import logging

def setup_logger():
    logger = logging.getLogger('gateway_logger')
    logger.setLevel(logging.INFO)

    #File Handler (write the logs to a file)
    file_handler = logging.FileHandler('gateway_logs.log')
    file_handler.setLevel(logging.INFO)

    # handle console output
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Formatter 
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

logger = setup_logger()

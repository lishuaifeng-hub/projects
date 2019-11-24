import logging
import logging.handlers

class Logger:
    def __init__(self, logger_name):
        self.logger = logging.getLogger(name=logger_name)
        self.logger.setLevel(logging.DEBUG)

        f_handler = logging.FileHandler(filename="error.log")
        f_handler.setLevel(logging.ERROR)
        f_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s%(funcName)s[:%(lineno)d] - %(message)s")
        f_handler.setFormatter(f_formatter)

        c_handler = logging.StreamHandler()
        c_handler.setLevel(logging.INFO)
        c_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        c_handler.setFormatter(c_formatter)

        self.logger.addHandler(f_handler)
        self.logger.addHandler(c_handler)

    def get_logger(self):
        return self.logger
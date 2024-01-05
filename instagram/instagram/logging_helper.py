
import logging
import os
from datetime import date


class Logger:
    def __init__(self, name):

        # create log directory in project
        self.log_folder = "logs"
        if not os.path.exists(self.log_folder):
            os.makedirs(self.log_folder)

        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        # formatter = logging.Formatter("%(pathname)s - %(funcName)s - %(lineno)d - %(asctime)s - %(levelname)s :%(message)s")
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

        # Create console handler and set level to DEBUG
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

        # Create file handler and set level to INFO
        log_file_name = os.path.join(self.log_folder, f"{date.today()}.log")
        fh = logging.FileHandler(log_file_name, mode='a')
        fh.setLevel(logging.INFO)
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)

    def log(self, level, message):
        if level == "debug":
            self.logger.debug(message)
        elif level == "info":
            self.logger.info(message)
        elif level == "warning":
            self.logger.warning(message)
        elif level == "error":
            self.logger.error(message)
        elif level == "critical":
            self.logger.critical(message)


logger = Logger(__name__)

if __name__ == "__main__":
    logger = Logger(__name__)
    logger.info("test")

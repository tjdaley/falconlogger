"""
flogger.py - Implements the FalconLogger class
"""
import logging
from dotenv import load_dotenv
import os

load_dotenv()

class FalconLogger(logging.Logger):
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL
    
    """Configures the logger based on the environment variables"""
    def __init__(self, name, level=None):
        super().__init__(name, level=level or self.get_log_level())
        console_handler = logging.StreamHandler()
        self.addHandler(console_handler)
        console_handler.setFormatter(logging.Formatter(self.get_format_string()))
        self.info('Logger initialized')

    def get_log_level(self):
        """Returns the log level based on the LOG_LEVEL environment variable"""
        log_level = os.getenv('LOG_LEVEL')
        if log_level == 'DEBUG':
            return logging.DEBUG
        elif log_level == 'INFO':
            return logging.INFO
        elif log_level == 'WARNING':
            return logging.WARNING
        elif log_level == 'ERROR':
            return logging.ERROR
        elif log_level == 'CRITICAL':
            return logging.CRITICAL
        else:
            return logging.INFO

    def get_format_string(self):
        """Returns the format string based on the LOG_FORMAT environment variable"""
        log_format = os.getenv('LOG_FORMAT')
        if log_format:
            return log_format

        systemd = os.getenv('STARTED_BY_SYSTEMD')
        if systemd:
            return '%(levelname)-8s - %(message)s'
        else:
            return '%(asctime)s - %(name)s - %(levelname)-8s - %(message)s'

def main():
    """Main function to test the FalconLogger class"""
    logger = FalconLogger('flogger')
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')

if __name__ == '__main__':
    main()

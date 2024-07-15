import logging


class Logger:
    def __init__(self, path, level='DEBUG'):
        logging.basicConfig(filename=path, level=level)
        self.logger = logging.getLogger(__name__)

    def connect(self):
        return self.logger

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)

if __name__ == '__main__':
    logger = Logger('log.txt')
    logger.info('Hello World')
    logger.warning('Hello World')
    logger.critical('Hello World')
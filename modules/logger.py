import logger

class Logger:
    def __init__(self, path):
        self.path = path

    def log(self, message):
        with open(self.path, 'a') as file:
            file.write(message + '\n')
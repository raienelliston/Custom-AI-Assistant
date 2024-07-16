import os
from config import Config
import threading
from logger import Logger

class ScriptHandler(threading.Thread):
    def __init__(self, output_queue):
        super().__init__()
        self.output_queue = output_queue
        self.logger = Logger.connect()

        for file in os.listdir('scripts'):
            if file.endswith('.py'):
                self.scripts.append(file)

    def run(self):
        exec(self.script)
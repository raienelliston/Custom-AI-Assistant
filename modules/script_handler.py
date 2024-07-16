import os
from config import Config
import threading
import importlib
from logger import Logger

config = Config()

class ScriptHandler(threading.Thread):
    def __init__(self, output_queue, timer):
        super().__init__()
        self.output_queue = output_queue
        self.logger = Logger.connect()
        self.timer = timer
        self.triggers = config.get_value('triggers', [])
        self.scripts = {}

        for file in os.listdir('scripts'):
            if file.endswith('.py'):
                self.scripts.append(file)

        for script in self.triggers:
            if script[1] not in self.scripts:
                self.logger.error(f"Script {script[1]} not found in scripts directory")
                self.triggers.remove(script)
            else:
                try:
                    module = importlib.import_module(f'scripts.{script[1]}')
                    function = getattr(module, 'run')
                    for trigger in script[0]:
                        self.triggers.append([trigger, function])
                    self.logger.info(f"Script {script[1]} loaded")
                except Exception as e:
                    self.logger.error(e)
            
        for script in self.scripts:
            if script not in self.triggers:
                self.logger.warning(f"Script {script} not in triggers")

    def run(self):
        self.running = True
        while self.running:
            try:
                data = self.output_queue.get()
                
                for script in self.triggers:
                    for trigger in script[0]:
                        if trigger in data:
                            self.scripts[script[1]](data)

            except Exception as e:
                self.logger.error(e)
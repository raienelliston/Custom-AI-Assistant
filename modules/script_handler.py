import os
from config import Config

class ScriptHandler:
    def __init__(self, script):
        self.script = script
        
        for file in os.listdir('scripts'):
            if file.endswith('.py'):
                self.scripts.append(file)

    def run(self):
        exec(self.script)
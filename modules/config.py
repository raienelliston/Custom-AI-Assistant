import os

filepath = os.path.abspath(__file__)

class Config:
    def __init__(self):
        self.config_path = os.path.join(os.path.dirname(filepath), 'config.txt')
        self.config = {}

    def get_config(self):
        with open(self.config_path, 'r') as file:
            for line in file:
                key, value = line.split('=')
                self.config[key] = value
    
    def set_value(self, key):
        try:
            self.config[key]
            exists = True
        except KeyError:
            exists = False

        if exists:
            pass
            return self.get_config()
        
        # Else
        pass
        return self.get_config()
    
    def get_value(self, key):
        try:
            return self.config[key]
        except KeyError:
            return None
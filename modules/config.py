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
    
    def set_value(self, key, value):
        try:
            self.config[key]
            with open(self.config_path, 'r') as file:
                for line in file:
                    if line.startswith(key):
                        line = f'{key}={value}\n'
                        file.write(line)
        except KeyError:
            with open(self.config_path, 'a') as file:
                file.write(f'{key}={value}\n')
        
        # Else
        pass
        return self.get_config()
    
    def get_value(self, key, default=None):
        try:
            return self.config[key]
        except KeyError:
            if default is not None:
                set_value(key, default)
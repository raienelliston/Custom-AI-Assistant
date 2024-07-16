import os

filepath = os.path.abspath(__file__)

class Config:
    def __init__(self):
        self.config_path = os.path.join(os.path.dirname(filepath), 'config.txt')
        self.config = {}
        self.config_list = []

    def get_config(self):
        with open(self.config_path, 'r') as file:
            for line in file:
                key, value = line.split('=')
                self.config[key] = value
                self.config_list.append(key)
    
    def set_value(self, key, value):
        all_config = ""

        # Finds all the config keys and values and writes them to the file
        for list_key in self.config_list:
            if list_key == key:
                all_config += f'{key}={value}\n'
            else:
                all_config += f'{list_key}={self.config[list_key]}\n'

        if not key in self.config_list:
            all_config += f'{key}={value}\n'

        with open(self.config_path, 'w') as file:
            file.write(all_config)
        
        self.config_list = []
        self.config[key] = value

    def get_value(self, key, default=None):
        try:
            return self.config[key]
        except KeyError:
            if default != None:
                self.set_value(key, default)
import time 

class Timestamp:
    def __init__(self):
        self.timestamp = time.perf_counter()

    def connect(self):
        return self 
    
    def get_timestamp(self):
        return time.perf_counter() - self.timestamp
import threading

class VoiceToText(threading.Thread):
    def __init__(self, input_queue, audio_device):
        super().__init__()
        self.input_queue = input_queue
        self.audio_device = audio_device
        self.running = False

    def get_audio_devices(self):
        pass

    def get_selected_audio_device(self):
        pass

    def set_audio_device(self, device):
        pass

    def start_listener(self):
        self.running = True
        

    def pause_listener(self):
        if self.running == False:
            print("Listener is already paused")
        self.running = False

    def unpause_listener(self):
        if self.running == True:
            print("Listener is already running")
            return
        self.running = True

    def stop_listener(self):
        self.running = False

    def convert(self, audio):
        return "Hello World"
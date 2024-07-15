import threading
import queue
import time
import keyboard
from modules.voice_to_text import VoiceToText
from modules.config import Config


class Assistant:
    def __init__(self):
        self.input_queue = queue.Queue()
        self.output_queue = queue.Queue()

    def start(self):
        pass

    def stop(self):
        pass

if __name__ == '__main__':
    config = Config()
    assistant = Assistant()
    assistant.start()
    while True:
        if keyboard.is_pressed('q'):
            assistant.stop()
            break
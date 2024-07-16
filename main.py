import threading
import queue
import time
import keyboard
from modules.voice_to_text import VoiceToText
from modules.text_handler import TextHandler
from modules.script_handler import ScriptHandler
from modules.config import Config

config = Config()

class Assistant:
    def __init__(self):
        # Initialize queues
        self.rawText = queue.Queue()
        self.commands = queue.Queue()

        # Initialize module classes
        self.voiceToText = VoiceToText(self.rawText, config.get_value('audio_device'))
        self.textHandler = TextHandler(self.rawText, self.commands)
        self.scriptHandler = ScriptHandler(self.commands)

    def start(self):
        self.voiceToText.start()
        self.textHandler.start()
        self.scriptHandler.start()

    def stop(self):
        self.voiceToText.stop()
        self.textHandler.stop()
        self.scriptHandler.stop()

if __name__ == '__main__':
    config = Config()
    assistant = Assistant()
    assistant.start()
    while True:
        if keyboard.is_pressed('q'):
            assistant.stop()
            break
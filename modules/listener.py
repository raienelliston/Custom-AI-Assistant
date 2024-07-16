import threading
import asyncio
import pyaudio
import wave
from config import Config

config = Config()

class Listener(threading.Thread):
    def __init__(self, input_queue=[]):
        super().__init__()
        self.input_queue = input_queue
        self.running = False

        self.set_settings()

    def set_settings(self):
        # Stop for safety
        self.running = False

        # Audio settings
        self.audio_device = config.get_value('audio_device', 0)
        self.format = config.get_value('format', 'int16')
        self.chunk = config.get_value('chunk', 1024)
        self.sample_rate = config.get_value('sample_rate', 44100)
        self.channels = config.get_value('channels', 2)
        self.pyaudio = pyaudio.PyAudio()

    def get_audio_devices(self):
        for i in range(self.pyaudio.get_device_count()):
            if self.pyaudio.get_device_info_by_index(i)["maxInputChannels"] > 0:
                print(i, self.pyaudio.get_device_info_by_index(i)["name"])

    async def start_listener(self):
        self.running = True
        self.stream = self.pyaudio.open(format=self.format,
                                    channels=self.channels,
                                    rate=self.sample_rate,
                                    input=True,
                                    input_device_index=self.audio_device,
                                    frames_per_buffer=self.chunk)
        await self.listen()

    async def _listen(self):
        while self.running:
            data = self.stream.read(self.chunk)
            print(data)
            self.input_queue.append(data)


    def stop_listener(self):
        self.running = False

if __name__ == '__main__':
    listen = Listener()
    listen.get_audio_devices()
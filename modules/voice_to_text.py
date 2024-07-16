import threading
import asyncio
import pyaudio
import wave
from config import Config

config = Config()

class VoiceToText(threading.Thread):
    def __init__(self, input_queue, audio_device):
        super().__init__()
        self.input_queue = input_queue
        self.audio_device = audio_device
        self.running = False

        # Audio settings
        self.format = config.get_value('format', 'int16')
        self.chunk = config.get_value('chunk', 1024)
        self.sample_rate = config.get_value('sample_rate', 44100)
        self.channels = config.get_value('channels', 2)
        self.pyaudio = pyaudio.PyAudio()

    def get_audio_devices(self):
        pass

    def get_selected_audio_device(self):
        pass

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
            self.input_queue.append(data)


    def stop_listener(self):
        self.running = False

if __name__ == '__main__':
    pass
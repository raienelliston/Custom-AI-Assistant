import threading
import asyncio
import wave
import sounddevice as sd
from config import Config
import numpy as np

config = Config()

class Listener(threading.Thread):
    def __init__(self, input_queue=[], timer=None):
        super().__init__()
        self.input_queue = input_queue
        self.running = False
        self.timer = timer

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
        self.frames = []

    def get_audio_devices(self):
        print(sd.query_devices())

    async def start_listener(self):
        self.running = True
        if self.audio_device == "default":
            self.stream = sd.InputStream(channels=self.channels, 
                                         samplerate=self.sample_rate, 
                                         blocksize=self.chunk,
                                         callback=self._write_block)
        else:
            self.stream = sd.InputStream(device=self.audio_device, 
                                        channels=self.channels, 
                                        samplerate=self.sample_rate, 
                                        blocksize=self.chunk,
                                        callback=self._write_block)
        self.stream.start()
        await self.listen()

    async def _listen(self):
        while self.running:
            data = self.stream.read(self.chunk)
            print(data)
            self.input_queue.append([data, self.timer.get_timestamp()])
        self.stream.stop()

    def _write_block(self, indata, frames, time, status):
        if status:
            print(status)

        self.frames.append(indata.copy())
        if len(self.frames) > self.chunk:
            block_data = np.concatenate(self.frames)
            self.input_queue.put(block_data)

    def stop_listener(self):
        self.running = False

if __name__ == '__main__':
    listen = Listener()
    listen.get_audio_devices()
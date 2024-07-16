import threading
import config as c
import speech_recognition as sr
import vosk as vk
import asyncio

config = c.Config()

class TextHandler(threading.Thread):
    def __init__(self, input_queue, output_queue, model_path=None):
        super().__init__()
        self.input_queue = input_queue
        self.output_queue = output_queue
        self.pause_amount = config.get_value('pause_amount', 0.5)

        self.seperated_audio = []
        self.saved_audio = []

        # Setup recognizer
        self.model_path = model_path
        self.api = model_path.split("_")[0]
        
        match self.api:
            case None:
                self.recognizer = sr.Recognizer()
            case "vosk":
                import vosk as vk
                self.recognizer = vk.KaldiRecognizer(vk.Model(self.model_path))

    async def run(self):
        self.running = True
        while self.running:
            try:
                text = await self.recognize(self.input_queue.get())
                if self.text != "":
                    pass
            except Exception as e:
                pass

    def recognize(self, audio):
        match self.api:
            case "vosk":
                return self.recognize_vosk(audio)

    def stop(self):
        self.running = False
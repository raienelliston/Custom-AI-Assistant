import threading
import config as c
import speech_recognition as sr
import vosk as vk
import asyncio

config = c.Config()

class TextHandler(threading.Thread):
    def __init__(self, input_queue, output_queue, timer, model_path=None):
        super().__init__()
        self.input_queue = input_queue
        self.output_queue = output_queue
        self.pause_amount = config.get_value('pause_amount', 0.5)
        self.timer = timer
        self.triggered = False
        self.min_length = config.get_value('min_word_command_length', 5)

        self.seperated_audio = []
        self.saved_audio = []
        self.seperated_text = []
        self.timestamps = []

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
                data = await self.input_queue.get()
                text = await self.recognize(data)
                if self.text != "":
                    self.seperated_text.append(text.split(" "))
                    self.timestamps.append(data[1])
                
                await self.filter_text()

            except Exception as e:
                pass

    def filter_text(self):
        words = [] * max(len(x) for x in self.seperated_text)
        for words in self.seperated_text:
            for index, word in enumerate(words):
                words[index].append(word)
 

 
        if len(words) > self.min_length:
            for word in words:
                if not self.triggered or word == "assistant":
                    words.pop(0)
                if word == "assistant":
                    self.triggered = True
                                    
                    
        


    def recognize(self, audio):
        match self.api:
            case "vosk":
                return self.recognize_vosk(audio)

    def stop(self):
        self.running = False
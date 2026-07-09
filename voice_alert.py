import threading

import pyttsx3


class VoiceAlert:

    def __init__(self):
        self.engine = pyttsx3.init()

        self.engine.setProperty("rate", 170)

        self.engine.setProperty("volume", 1)

    def speak(self, text):

        thread = threading.Thread(
            target=self._run,
            args=(text,),
            daemon=True
        )

        thread.start()

    def _run(self, text):

        self.engine.say(text)

        self.engine.runAndWait()
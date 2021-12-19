from multiprocessing import Pipe
import subprocess
import tempfile


VOICES = ['de-DE', 'en-GB', 'en-US', 'es-ES', 'fr-FR', 'it-IT']
CHUNK = 1024


class Mouth:

    def __init__(self, voice='de-DE') -> None:
        self._voice = voice
        self.pipe = None

    def run(self, pipe) -> None:
        ...

    def speak(self, text):
        wf = self._create_wave(text)
        # todo: send to main thread


    def _create_wave(self, txt):
        with tempfile.NamedTemporaryFile(suffix='.wav') as f:
            cmd = [
                'pico2wave', 
                '-l',
                self._voice, 
                '-w',
                f.name,
                txt.encode('utf8')
            ]
            subprocess.call(cmd)
            f.seek(0)
            return f.read()

    @property
    def voices(self) -> list:
        return VOICES

    @property
    def voice(self) -> str:
        return self._voice

    @voice.setter
    def voice(self, v) -> None:
        if v in VOICES:
            self._voice = v
        else:
            print("Unknown voice, supported voices:{voices}".format(voices=VOICES))
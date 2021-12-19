from multiprocessing import Pipe
import subprocess
import tempfile


VOICES = ['de-DE', 'en-GB', 'en-US', 'es-ES', 'fr-FR', 'it-IT']
CHUNK = 1024


class Mouth:

    def __init__(self, voice='de-DE') -> None:
        """ Initialize the mouth module. """
        print("INFO: Initializing mouth")
        print(f"INFO: Setting voice to {voice}")
        self._voice = voice
        print("INFO: Done initializing mouth")

    def handle(self, text) -> None:
        """ Handle the given text."""
        return self._create_wave(text)

    def _create_wave(self, txt):
        """ Create a wave file from the given text. """
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
        """ Get a list of available voices. """
        return VOICES

    @property
    def voice(self) -> str:
        """ Get the current voice. """
        return self._voice

    @voice.setter
    def voice(self, v) -> None:
        """ Set the current voice. """
        if v in VOICES:
            self._voice = v
        else:
            print("WARNING: Unknown voice, supported voices:{voices}".format(voices=VOICES))
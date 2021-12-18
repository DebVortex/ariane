from io import BytesIO
import json

from PIL import Image
from websocket import WebSocketApp
import numpy as np

from ariane.modules.eyes import Eyes
from ariane.modules.mouth import Mouth

class Ariane:

    def __init__(self) -> None:
        self.eyes = Eyes()
        self.mouth = Mouth()
        self.ws = WebSocketApp(
            'ws://localhost:3001',
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close
        )
        self.ws.on_open = self.on_open

    def run(self) -> None:
        self.ws.run_forever()

    def on_open(self) -> None:
        print("INFO: Connection establisted.")

    def on_close(self) -> None:
        print("INFO: Connection closed.")

    def on_error(self, err) -> None:
        print("ERROR: ", err)

    def on_message(self, buff) -> None:
        stream = BytesIO(buff)
        img = Image.open(stream).convert("RGB")
        img_array = np.array(img, dtype=np.uint8)
        persons = self.eyes.handle(img_array)
        print('INFO: sending persons ', persons)
        self.ws.send(json.dumps(persons))

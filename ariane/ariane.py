from io import BytesIO
import json

from PIL import Image
import numpy as np

from simple_websocket_server import WebSocket


from modules.eyes import Eyes
from modules.mouth import Mouth


class WebSocketHandler(WebSocket):

    def __init__(self, *args: list, **kwargs: dict) -> None:
        self.ariane = Ariane()
        super().__init__(*args, **kwargs)

    def connected(self) -> None:
        print(self.address, 'connected')

    def handle_close(self) -> None:
        print(self.address, 'closed')

    def handle(self, buff) -> None:
        stream = BytesIO(buff)
        img = Image.open(stream).convert("RGB")
        img_array = np.array(img, dtype=np.uint8)
        persons = self.ariane.eyes.handle(img_array)
        print('INFO: sending persons ', persons)
        self.ws.send(json.dumps(persons))


class Ariane:

    def __init__(self, host="", port=8080) -> None:
        self.eyes = Eyes()
        self.mouth = Mouth()

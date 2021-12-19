from io import BytesIO
import json

from PIL import Image
import numpy as np
from simple_websocket_server import WebSocket

from ariane import Ariane


ariane = Ariane()


class WebSocketHandler(WebSocket):

    def __init__(self, *args: list, **kwargs: dict) -> None:
        super().__init__(*args, **kwargs)

    def connected(self) -> None:
        print(self.address, 'connected')

    def handle_close(self) -> None:
        print(self.address, 'closed')

    def handle(self, buff) -> None:
        stream = BytesIO(buff)
        img = Image.open(stream).convert("RGB")
        img_array = np.array(img, dtype=np.uint8)
        persons = ariane.eyes.handle(img_array)
        print('INFO: sending persons ', persons)
        self.ws.send(json.dumps(persons))
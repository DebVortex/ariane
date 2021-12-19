
from modules.eyes import Eyes
from modules.mouth import Mouth
from modules.ears import Ears


class Ariane:

    def __init__(self) -> None:
        self.eyes = Eyes()
        self.mouth = Mouth()
        self.ears = Ears()

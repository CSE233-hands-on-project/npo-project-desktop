from abc import ABC, abstractmethod
from views.abstractview import AbstractView


class AbstractController(ABC):
    def __init__(self):
        self.view: AbstractView = None
        super().__init__()

    @abstractmethod
    def start(self): pass

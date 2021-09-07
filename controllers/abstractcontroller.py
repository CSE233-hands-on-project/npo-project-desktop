from abc import ABC, abstractmethod
from tkinter import Button


class AbstractController(ABC):
    def __init__(self, toggler=None):
        self.toggler = toggler
        self.view = None
        super().__init__()

    @abstractmethod
    def start(self): pass
    def toggle(self): pass

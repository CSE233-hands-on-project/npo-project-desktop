from tkinter import Label
from .abstracttoggleableview import AbstractToggleableView


class View(AbstractToggleableView):

    def launch(self):
        Label(self.root, text=str(self.parentcontroller)).pack(pady=128, padx=32)

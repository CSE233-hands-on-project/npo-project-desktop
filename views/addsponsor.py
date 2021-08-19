from tkinter import *


class View():
    def __init__(self):
        self.display = None

    def toggle(self):
        if self.display: self.display.destroy(); self.display = None
        else:
            self.display = Tk()
            Label(self.display, text=__name__).pack()

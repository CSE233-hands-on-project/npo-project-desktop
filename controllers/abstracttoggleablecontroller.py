
from tkinter import Button
from views.abstracttoggleableview import AbstractToggleableView
from .abstractcontroller import AbstractController
from models import constants as c


class AbstractToggleableController(AbstractController):
    def __init__(self, toggler):
        super().__init__()
        self.toggler = toggler

    def toggle(self):
        self.view: AbstractToggleableView; self.toggler: Button  # Typehinting

        self.view.toggle()

        try: self.toggler.configure(bg=c.get_color("active")
                                    if self.toggler.cget("bg") == c.get_color("idle")
                                    else c.get_color("idle"))
        except Exception: pass  # HACK: Dirty workaround for silencing exceptions regarding modifying destroyed button

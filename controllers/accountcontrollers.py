from .abstractcontroller import AbstractController
from views import placeholder
from tkinter import Button


class ManageMembers(AbstractController):
    def __init__(self, toggler): super().__init__(toggler=toggler)
    def start(self): self.view = placeholder.View(parentcontroller=self)

    def toggle(self):
        self.view.toggle()
        try: self.toggler.configure(bg="lightgreen" if self.toggler.cget("bg") == "lightgrey" else "lightgrey")
        except Exception: pass


class AdjustRoles(AbstractController):
    def __init__(self, toggler): super().__init__(toggler=toggler)
    def start(self): self.view = placeholder.View(parentcontroller=self)

    def toggle(self):
        self.view.toggle()
        try: self.toggler.configure(bg="lightgreen" if self.toggler.cget("bg") == "lightgrey" else "lightgrey")
        except Exception: pass


class ChangePass(AbstractController):
    def __init__(self, toggler): super().__init__(toggler=toggler)
    def start(self): self.view = placeholder.View(parentcontroller=self)

    def toggle(self):
        self.view.toggle()
        try: self.toggler.configure(bg="lightgreen" if self.toggler.cget("bg") == "lightgrey" else "lightgrey")
        except Exception: pass


class ApprovePass(AbstractController):
    def __init__(self, toggler): super().__init__(toggler=toggler)
    def start(self): self.view = placeholder.View(parentcontroller=self)

    def toggle(self):
        self.view.toggle()
        try: self.toggler.configure(bg="lightgreen" if self.toggler.cget("bg") == "lightgrey" else "lightgrey")
        except Exception: pass

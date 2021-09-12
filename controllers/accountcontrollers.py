from .abstracttoggleablecontroller import AbstractToggleableController
from views import placeholder


class ManageMembers(AbstractToggleableController):
    def __init__(self, toggler): super().__init__(toggler=toggler)
    def start(self): self.view = placeholder.View(parentcontroller=self)


class AdjustRoles(AbstractToggleableController):
    def __init__(self, toggler): super().__init__(toggler=toggler)
    def start(self): self.view = placeholder.View(parentcontroller=self)


class ChangePass(AbstractToggleableController):
    def __init__(self, toggler): super().__init__(toggler=toggler)
    def start(self): self.view = placeholder.View(parentcontroller=self)


class ApprovePass(AbstractToggleableController):
    def __init__(self, toggler): super().__init__(toggler=toggler)
    def start(self): self.view = placeholder.View(parentcontroller=self)

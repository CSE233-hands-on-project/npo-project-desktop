from .abstracttoggleablecontroller import AbstractToggleableController
from views import placeholder


class RequestEvent(AbstractToggleableController):
    def __init__(self, toggler): super().__init__(toggler=toggler)
    def start(self): self.view = placeholder.View(parentcontroller=self)


class ApproveEventRequest(AbstractToggleableController):
    def __init__(self, toggler): super().__init__(toggler=toggler)
    def start(self): self.view = placeholder.View(parentcontroller=self)


class ViewEvents(AbstractToggleableController):
    def __init__(self, toggler): super().__init__(toggler=toggler)
    def start(self): self.view = placeholder.View(parentcontroller=self)

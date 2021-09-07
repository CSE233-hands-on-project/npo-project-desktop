from importlib import import_module
from tkinter import Label, Message, Button

from models.user import User
from models.usertype import UserType
from .abstractview import AbstractView
from controllers.abstractcontroller import AbstractController


class UserDashboard(AbstractView):
    def __init__(self, user: User, parentcontroller: AbstractController):
        self.user = user
        super().__init__(parentcontroller)

    def launch(self):

        self.root.resizable(False, False)
        self.root.title('CSE233 Project - User Dashboard')
        welcome_label = Label(self.root, text=f'Welcome, {self.user.type.name}...', width=65)
        name_label = Label(self.root, text=self.user.fullname, font="Times 12 bold italic")
        msg = Message(self.root, width=400, fg="blue", text="Please pick an option...")

        welcome_label.grid(row=self.r(), pady=[32, 0])
        name_label.grid(row=self.r(), pady=[0, 20])

        module: UserType.AccessibleModule  # Typehinting
        for module in self.user.type.accessiblemodules:

            # Import the module that has the same name as that in the current user type's accessible modules list item
            # The module is described via its parent package and class name
            try:
                controllermodule = import_module('.' + module.packagename(), "controllers")
                Controller = getattr(controllermodule, module.classname)
            except Exception as e:
                print(f"Exception occured during importing {module.packagename()}.{module.classname}")
                print("Couldn't import package or class...")
                print(f"{str(e)}\n\n")
                continue

            # Create a button that will be dedicated for toggling this module on or off (and reflects its state)
            b = Button(self.root, text=module.displayname, width=32, bg="lightgrey", relief="groove")

            # Start the controller with its toggle control assigned to the button
            controller: AbstractController = Controller(toggler=b)
            b.configure(command=controller.toggle)
            controller.start()

            # A module description area is also to be displayed at the bottom of the dashboard upon mouse hover
            b.bind("<Enter>", lambda event, t=module.description: msg.config(text=t))
            b.bind("<Leave>", lambda event: msg.config(text=""))
            b.grid(row=self.r(), pady=4)

            # Explaining some weird aspects regarding the use of lambda above
            # https://realpython.com/python-lambda/#evaluation-time
            # https://realpython.com/python-lambda/#closure
            # Using a variable directly would make to the lambda function evaluate its value *during execution*
            # In other words, it will not fetch/store the value of the variable during *function definition*
            # Since this is a loop, the last value for any variable is the last value it has in the loop
            # Accordingly, whenever the lambda function is executed later, it will fetch that last value
            # Second point is the unused "event"
            # The bind function requires its function argument to itself take an "event" argument

        msg.grid(row=self.r(), pady=16)

        self.root.eval('tk::PlaceWindow . center')  # Center the window

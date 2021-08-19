from tkinter import *
from models.user import User
from views import signin_panel
from importlib import import_module


def launch(user: User):

    dashboard = Tk()
    dashboard.resizable(FALSE, FALSE)
    dashboard.title('CSE233 Project - User Dashboard')
    welcome_label = Label(dashboard, text=f'Welcome, {user.usertype}...', width=65); welcome_label.pack(pady=[32, 0])
    name_label = Label(dashboard, text=user.fullname, font="Times 12 bold italic"); name_label.pack(pady=[0, 20])
    msg = Message(dashboard, width=400, fg="blue", text="Please pick an option...")  # won't pack here yet

    for view in user.accessibleviews:

        # Import the module that has the same pathnamecode (column #3) as that in the user's accessible views list item
        try: module = import_module('.' + view[2], "views")
        except: pass

        # Create a button per module that toggles the module and it itself gets toggled upon click
        # Also, per button, a view corresponding to the imported module is created and manipulated
        b = Button(dashboard, text=view[1], width=32, bg="lightgrey", relief="groove", command=module.View().toggle)
        b.bind("<1>", lambda event, b=b: b.config(bg="lightgreen" if b.cget("bg") == "lightgrey" else "lightgrey"))

        # A module description area is also to be displayed at the bottom of the dashboard
        b.bind("<Enter>", lambda event, t=view[3]: msg.config(text=t))
        b.bind("<Leave>", lambda event: msg.config(text=""))
        b.pack(pady=4)

        # Explaining some weird aspects regarding the use of lambda above
        # https://realpython.com/python-lambda/#evaluation-time
        # https://realpython.com/python-lambda/#closure
        # Using a variable directly would make to the lambda function evaluate its value *during execution*
        # In other words, it will not fetch/store the value of the variable during *function definition*
        # Since this is a loop, the last value for any variable is the last value it has in the loop
        # Accordingly, whenever the lambda function is executed later, it will fetch that last value
        # Second point is the unused "event"
        # The bind function requires its function argument to itself take an "event" argument

    msg.pack(pady=16)

    def switch_to_login_panel():
        dashboard.destroy(); signin_panel.launch()

    return_button = Button(dashboard, text="Back to login page", width=20, command=switch_to_login_panel)
    return_button.pack(pady=[0, 32])

    dashboard.eval('tk::PlaceWindow . center')  # Center the window

    mainloop()  # infinite loop to keep window open

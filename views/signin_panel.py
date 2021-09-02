from tkinter import Frame, ttk, Label, Entry, Button, PhotoImage

from controllers import userlogin
from .abstractview import AbstractView


class SigninPanel(AbstractView):

    def launch(self):

        self.root.title('CSE233 Project - Landing Page')
        self.build_header()
        self.build_form()
        self.build_extras()

        for i in range(self.r()): self.root.rowconfigure(i, weight=1)  # Make rows span full width
        for i in range(self.c()): self.root.columnconfigure(i, weight=1)  # Make columns span full height

        self.root.eval('tk::PlaceWindow . center')  # Center the window

    def build_header(self):

        # Store the image as an attribute of this object (otherwise it gets garbage collected and can't be used)
        self.headerimage = PhotoImage(file="./assets/Charity.png")
        image = Label(self.root, image=self.headerimage)
        desc1 = Label(self.root, text="Welcome to your organization management portal", font="Times 16")
        desc2 = Label(self.root, text="Please enter your username and password below", font="Calibri 12")

        image.grid(row=self.r(), column=0, columnspan=3, pady=20)  # Place image in the first row
        desc1.grid(row=self.r(), column=0, columnspan=3, padx=40)  # Place description 1 below it
        desc2.grid(row=self.r(), column=0, columnspan=3, pady=[0, 20])  # Place description 2 below it

    def build_form(self):

        def signin():

            sign_in_button.config(state="disabled")
            response_label.config(text="Loading...", fg="blue")

            self.root.update()  # Required to display the "Loading..." text while it actually loads

            try: userlogin.attempt(username_entry.get(), password_entry.get())
            except ValueError as e:
                sign_in_button.config(state="normal")
                response_label.config(text=str(e), fg="red")

        username_label = Label(self.root, text="Username:", font="Calibri 12")
        username_entry = Entry(self.root, width=50); username_entry.focus()
        password_label = Label(self.root, text="Password:", font="Calibri 12")
        password_entry = Entry(self.root, width=50, show="*")
        sign_in_button = Button(self.root, width=40, text="Sign in", font="Calibri 12", command=signin)
        response_label = Label(self.root, text="")
        self.root.bind("<Return>", lambda event: signin())

        username_label.grid(row=self.r(), column=0, pady=5)
        username_entry.grid(row=self.r() - 1, column=1, padx=[0, 40], columnspan=2, sticky="ew")
        password_label.grid(row=self.r(), column=0, pady=5)
        password_entry.grid(row=self.r() - 1, column=1, padx=[0, 40], columnspan=2, sticky="ew")
        sign_in_button.grid(row=self.r(), column=0, pady=[20, 5], columnspan=3)
        response_label.grid(row=self.r(), column=0, pady=[5, 20], columnspan=3)

    def build_extras(self):

        # Extra features section for academic project purposes (not actually required by organization)
        ttk.Separator(self.root, orient='horizontal').grid(sticky="nsew",
                                                           row=self.r(),
                                                           columnspan=self.c() if self.c() else 1)
        eval_label = Label(self.root, text="For demonstration purposes only...", font=('Calibri Light', 10), fg="grey")
        eval_label.grid(row=self.r(), columnspan=self.c() if self.c() else 1, pady=5)

        # Creating a frame to contain two buttons side-by-side
        extras = Frame(self.root)
        donation_button = Button(extras, text="Donate now", width=20, borderwidth=1, command=userlogin.donate)
        register_button = Button(extras, text="Register for an event (WIP)", width=20, borderwidth=1, state='disabled')
        donation_button.grid(row=0, column=0, padx=5)
        register_button.grid(row=0, column=1, padx=5)

        # Placing the frame on the grid in a new row, with full span
        extras.grid(row=self.r(), pady=[0, 20], columnspan=self.c() if self.c() else 1)

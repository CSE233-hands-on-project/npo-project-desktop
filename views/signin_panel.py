from tkinter import Frame, ttk, Label, Entry, Button, PhotoImage
from .abstractview import AbstractView
from models import constants as c


class SigninPanel(AbstractView):

    def launch(self):

        self.root.title(c.get_prompt("signintitle"))
        self.build_header()
        self.build_form()
        self.build_extras()

        for i in range(self.r()): self.root.rowconfigure(i, weight=1)  # Make rows span full width
        for i in range(self.c()): self.root.columnconfigure(i, weight=1)  # Make columns span full height

        # Center the window and set its min and max dimensions
        self.root.eval('tk::PlaceWindow . center')
        self.root.minsize(self.root.winfo_reqwidth(), self.root.winfo_reqheight())
        self.root.maxsize(self.root.winfo_reqwidth() * 2, int(self.root.winfo_reqheight() * 1.2))

    def build_header(self):

        # Store the image as an attribute of this object (otherwise it gets garbage collected and can't be used)
        self.headerimage = PhotoImage(file="./assets/Charity.png")
        image = Label(self.root, image=self.headerimage)
        desc1 = Label(self.root, text=c.get_prompt("signindesc1"), font=c.get_font("primary"))
        desc2 = Label(self.root, text=c.get_prompt("signindesc1"), font=c.get_font("secondary"))

        image.grid(row=self.r(), column=0, columnspan=3, pady=20)  # Place image in the first row
        desc1.grid(row=self.r(), column=0, columnspan=3, padx=40)  # Place description 1 below it
        desc2.grid(row=self.r(), column=0, columnspan=3, pady=[0, 20])  # Place description 2 below it

    def build_form(self):

        def signin():

            sign_in_button.config(state="disabled")
            response_label.config(text=c.get_prompt("loadingprompt"), fg=c.get_color("information"))

            self.root.update()  # Required to display the "Loading..." text while it actually loads

            try: self.parentcontroller.attemptlogin(username_entry.get(), password_entry.get())
            except ValueError as e:
                sign_in_button.config(state="normal")
                response_label.config(text=str(e), fg=c.get_color("error"))

        username_label = Label(self.root, text=c.get_prompt("usernamelabel"), font=c.get_font("secondary"))
        username_entry = Entry(self.root, width=50); username_entry.focus()
        password_label = Label(self.root, text=c.get_prompt("passwordlabel"), font=c.get_font("secondary"))
        password_entry = Entry(self.root, width=50, show="*")
        sign_in_button = Button(self.root, width=40, text=c.get_prompt(
            "signinbuttonlabel"), font=c.get_font("secondary"), command=signin)
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
        eval_label = Label(self.root, text=c.get_prompt("noaccprompt"),
                           font=f'{c.get_font("secondary")} italic', fg=c.get_color("secondarydark"))
        eval_label.grid(row=self.r(), columnspan=self.c() if self.c() else 1, pady=5)

        # Creating a frame to contain two buttons side-by-side
        extras = Frame(self.root)
        volunteer_button = Button(extras, text=c.get_prompt("volunteerbuttonlabel"),
                                  width=24, borderwidth=1, state='disabled')
        register_button = Button(extras, text=c.get_prompt("registerbuttonlabel"),
                                 width=24, borderwidth=1, state='disabled')
        volunteer_button.grid(row=0, column=0, padx=5)
        register_button.grid(row=0, column=1, padx=5)

        # Placing the frame on the grid in a new row, with full span
        extras.grid(row=self.r(), pady=[0, 20], columnspan=self.c() if self.c() else 1)

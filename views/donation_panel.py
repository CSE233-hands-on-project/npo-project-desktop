from tkinter import Label, Button, Entry, Listbox, Radiobutton, IntVar
from .abstracttoggleableview import AbstractToggleableView
from models import constants as c


class DonationPanel(AbstractToggleableView):
    def __init__(self, parentcontroller, eventtypenames, pmnames):
        super().__init__(parentcontroller)  # TODO: typehint that parentcontroller is MakeDonation
        self.eventtypenames = eventtypenames
        self.pmnames = pmnames

    def launch(self):
        super().launch()
        self.root.resizable(False, False)
        self.root.title(c.get_prompt("donationpaneltitle"))
        self.show_donation_menu()

    def show_donation_menu(self):
        self.dm_event_label = Label(self.root, text=c.get_prompt("eventselect"))
        self.dm_event_lstbx = Listbox(self.root, selectmode="single",
                                      height=len(self.eventtypenames), exportselection=0)
        for n in self.eventtypenames: self.dm_event_lstbx.insert("end", n[0])

        self.donationchoice = IntVar(self.root)
        self.donationchoice.set(3)

        self.dm_money_rdbtn = Radiobutton(self.root, text=c.get_prompt("moneycategory"),
                                          variable=self.donationchoice, value=1,
                                          command=self.parentcontroller.setdonationtypechoice)

        self.dm_money_lstbx = Listbox(self.root, selectmode="single", height=len(self.pmnames), exportselection=0)
        for n in self.pmnames: self.dm_money_lstbx.insert("end", n[0])
        self.dm_money_lstbx.configure(state="disabled")
        self.dm_money_lstbx.bind("<<ListboxSelect>>", lambda e:
                                 self.proceed_btn.configure(state="normal"
                                                            if self.dm_money_lstbx.curselection()
                                                            else "disabled"))

        self.dm_items_rdbtn = Radiobutton(self.root, text=c.get_prompt("itemcategory"),
                                          variable=self.donationchoice, value=2,
                                          command=self.parentcontroller.setdonationtypechoice)

        self.dm_items_lstbx = Listbox(self.root, selectmode="single", height=3, exportselection=0)
        for item in ("item1", "item2", "item3"): self.dm_items_lstbx.insert("end", item)
        self.dm_items_lstbx.configure(state="disabled")
        self.dm_items_lstbx.bind("<<ListboxSelect>>", lambda e:
                                 self.proceed_btn.configure(state="normal"
                                                            if self.dm_items_lstbx.curselection()
                                                            else "disabled"))

        self.proceed_btn = Button(self.root, text="Proceed", bg="white", state="disabled",
                                  command=self.parentcontroller.pay)

        self.donation_steps = Label(self.root, text=c.get_prompt("donationsteps"), pady=40)
        self.donation_steps.grid(row=self.r(), columnspan=3)
        self.dm_event_label.grid(row=self.r(), column=0, columnspan=3, pady=[20, 0])
        self.dm_event_lstbx.grid(row=self.r(), column=1, pady=[8, 32], padx=32)
        self.dm_money_rdbtn.grid(row=self.r(), column=0)
        self.dm_items_rdbtn.grid(row=self.r() - 1, column=2)
        self.dm_money_lstbx.grid(row=self.r(), column=0, pady=[8, 32], padx=32)
        self.dm_items_lstbx.grid(row=self.r() - 1, column=2, pady=[8, 32], padx=32)
        self.proceed_btn.grid(row=self.r() - 1, column=1, sticky="nsew", pady=[0, 20])

    def show_payment_menu(self, paymentmethodoptions):

        formfields = []

        option: str  # Typehinting that all "options" are string values
        for option in paymentmethodoptions:

            Label(self.root, text=option[0], width=64).grid(row=self.r(), padx=16, pady=[16, 0])
            
            if "Listbox:" in option[1]:  # If part of the option name is "Listbox:"
                listboxvals = self.parentcontroller.get_all_names_of(option[1].removeprefix("Listbox:"))
                field = Listbox(self.root, height=len(listboxvals), width=32, exportselection=0)
                for i in listboxvals: field.insert("end", i[0])  # Insert at the end of the listbox each value
                field.grid(row=self.r())

            else: field = Entry(self.root, width=32); field.grid(row=self.r())

            formfields.append(field)

        Button(self.root, text=c.get_prompt("submit"), pady=8, padx=16, command=lambda:
               self.parentcontroller.succeed(formfields, paymentmethodoptions)
               ).grid(row=self.r(), pady=[32, 16])

        Button(self.root, text=c.get_prompt("cancel"), pady=8, padx=16,
               command=self.parentcontroller.cancelpay).grid(row=self.r(), pady=[16, 32])

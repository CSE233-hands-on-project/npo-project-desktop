from tkinter import Label, Button, Entry, Listbox, Radiobutton, IntVar
from .abstractview import AbstractView


class DonationPanel(AbstractView):

    def launch(self, eventtypenames, pmnames):
        super().launch()
        self.root.resizable(False, False)
        self.root.title('Donation Panel')
        self.show_donation_menu(eventtypenames, pmnames)

    def show_donation_menu(self, eventtypenames, pmnames):
        self.dm_event_label = Label(self.root, text="Choose an event to donate for:")
        self.dm_event_lstbx = Listbox(self.root, selectmode="single", height=len(eventtypenames), exportselection=0)
        for n in eventtypenames: self.dm_event_lstbx.insert("end", n[0])

        self.donationchoice = IntVar(self.root)
        self.donationchoice.set(3)

        self.dm_money_rdbtn = Radiobutton(self.root, text="Donate with money:", variable=self.donationchoice, value=1,
                                          command=self.parentcontroller.setdonationtypechoice)

        self.dm_money_lstbx = Listbox(self.root, selectmode="single", height=len(pmnames), exportselection=0)
        for n in pmnames: self.dm_money_lstbx.insert("end", n[0])
        self.dm_money_lstbx.configure(state="disabled")

        self.dm_items_rdbtn = Radiobutton(self.root, text="Donate with items:", variable=self.donationchoice, value=2,
                                          command=self.parentcontroller.setdonationtypechoice)

        self.dm_items_lstbx = Listbox(self.root, selectmode="single", height=3, exportselection=0)
        for n in ("item1", "item2", "item3"): self.dm_items_lstbx.insert("end", n)
        self.dm_items_lstbx.configure(state="disabled")

        self.go_btn = Button(self.root, text="Go", bg="white", command=self.parentcontroller.pay)

        self.dm_event_label.grid(row=self.r(), column=0, columnspan=3, pady=[20, 0])
        self.dm_event_lstbx.grid(row=self.r(), column=1, pady=[8, 32], padx=32)
        self.dm_money_rdbtn.grid(row=self.r(), column=0)
        self.dm_items_rdbtn.grid(row=self.r() - 1, column=2)
        self.dm_money_lstbx.grid(row=self.r(), column=0, pady=[8, 32], padx=32)
        self.dm_items_lstbx.grid(row=self.r() - 1, column=2, pady=[8, 32], padx=32)
        self.go_btn.grid(row=self.r() - 1, column=1, sticky="nsew", pady=[0, 20])

    def hide_donation_menu(self):
        self.dm_event_label.grid_forget()
        self.dm_event_lstbx.grid_forget()
        self.dm_money_rdbtn.grid_forget()
        self.dm_items_rdbtn.grid_forget()
        self.dm_money_lstbx.grid_forget()
        self.dm_items_lstbx.grid_forget()
        self.go_btn.grid_forget()

    def show_payment_menu(self, paymentmethodoptions):

        formfields = []

        for d in paymentmethodoptions:

            Label(self.root, text=d[0], width=64).pack(padx=16, pady=[16, 0])
            if "Listbox" in d[1]:
                listitems = self.parentcontroller.get_all_names_of(d[1][d[1].find(":") + 1:])
                l = Listbox(self.root, height=len(listitems), width=32, exportselection=0)
                for i in listitems: l.insert("end", i[0])
                l.pack(); formfields.append(l)

            else: e = Entry(self.root, width=32); e.pack(); formfields.append(e)

        Button(self.root, text="Submit", pady=8, padx=16, command=lambda:
               self.parentcontroller.succeed(formfields, paymentmethodoptions)
               ).pack(pady=[32, 16])

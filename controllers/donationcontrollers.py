from models.paymentmethod import PaymentMethod
from models.eventtype import EventType
from models.__init__ import dbconnection as db  # FIXME: Should not call db in controller!

from .abstractcontroller import AbstractController

from views.donation_panel import DonationPanel
from views import placeholder
from tkinter import Button


class MakeDonation(AbstractController):
    def __init__(self, toggler): super().__init__(toggler=toggler)

    def start(self): self.view = DonationPanel(parentcontroller=self, startwith__init__=False)

    def toggle(self):
        self.toggler: Button
        if self.toggler.cget("bg") == "lightgrey":
            self.toggler.configure(bg="lightgreen")
            self.view.launch(EventType.get_all_event_type_names(), PaymentMethod.get_all_pm_names())
        else:
            self.toggler.configure(bg="lightgrey")
            self.view.root.destroy()
            self.view.root = None

    def setdonationtypechoice(self):
        if self.view.donationchoice.get() == 1:
            self.view.dm_money_lstbx.configure(state="normal")
            self.view.dm_items_lstbx.selection_clear(0, "end")
            self.view.dm_items_lstbx.configure(state="disabled")
        elif self.view.donationchoice.get() == 2:
            self.view.dm_items_lstbx.configure(state="normal")
            self.view.dm_money_lstbx.selection_clear(0, "end")
            self.view.dm_money_lstbx.configure(state="disabled")
        else:
            self.view.dm_items_lstbx.selection_clear(0, "end")
            self.view.dm_money_lstbx.selection_clear(0, "end")
            self.view.dm_items_lstbx.configure(state="disabled")
            self.view.dm_money_lstbx.configure(state="disabled")

    def pay(self):
        paymentmethodid = self.view.dm_money_lstbx.curselection()[0] + 1
        paymentmethod = PaymentMethod(paymentmethodid)
        paymentmethod.build()
        self.view.hide_donation_menu()
        self.view.show_payment_menu(paymentmethod.options)

    def get_all_names_of(arg):
        return db.submit_query(f"SELECT name FROM {arg}")

    def succeed(self, fields, paymentmethodoptions):

        import re

        values = []

        for i in range(len(paymentmethodoptions)):

            if paymentmethodoptions[i][1] == "String" and re.fullmatch("[a-zA-Z ]+", fields[i].get()):
                values.append(fields[i].get())

            elif paymentmethodoptions[i][1] == "Number" and re.fullmatch("[0-9]+", fields[i].get()):
                values.append(int(fields[i].get()))

            elif paymentmethodoptions[i][1] == "MonthYear" and re.fullmatch("[0-3][0-9]\/[0-9][0-9]", fields[i].get()):
                values.append(fields[i].get())

            elif paymentmethodoptions[i][1] == "Email" and re.fullmatch(
                    "[a-zA-Z0-9\._-]+@([a-zA-Z0-9_-]+\.)+[a-zA-Z0-9_-]{2,4}", fields[i].get()
            ):
                values.append(fields[i].get())

            elif "Listbox" in paymentmethodoptions[i][1] and fields[i].curselection():
                values.append(fields[i].curselection()[0])

            else: break

        else: print(values)  # TODO: Insert values into db instead of printing values (simple)


class ViewPrevDonations(AbstractController):
    def __init__(self, toggler): super().__init__(toggler=toggler)
    def start(self): self.view = placeholder.View(parentcontroller=self)

    def toggle(self):
        self.view.toggle()
        try: self.toggler.configure(bg="lightgreen" if self.toggler.cget("bg") == "lightgrey" else "lightgrey")
        except Exception: pass


class ViewDonations(AbstractController):
    def __init__(self, toggler): super().__init__(toggler=toggler)
    def start(self): self.view = placeholder.View(parentcontroller=self)

    def toggle(self):
        self.view.toggle()
        try: self.toggler.configure(bg="lightgreen" if self.toggler.cget("bg") == "lightgrey" else "lightgrey")
        except Exception: pass

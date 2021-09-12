from models.paymentmethods import PaymentMethod
from models.eventtypes import EventType

from .abstracttoggleablecontroller import AbstractToggleableController

from views.donation_panel import DonationPanel
from views import placeholder


class MakeDonation(AbstractToggleableController):
    def __init__(self, toggler): super().__init__(toggler=toggler)

    def start(self): self.view = DonationPanel(parentcontroller=self,
                                               eventtypenames=EventType.get_all_names(),
                                               pmnames=PaymentMethod.get_all_names())

    def setdonationtypechoice(self):
        self.view: DonationPanel
        if self.view.dm_event_lstbx.curselection():
            self.view.proceed_btn.configure(state="disabled")
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
        else: self.view.donationchoice.set(3)

    def pay(self):
        paymentmethodid = self.view.dm_money_lstbx.curselection()[0] + 1  # convert starting index 0->1
        paymentmethod = PaymentMethod(paymentmethodid)
        paymentmethod.build()
        self.view.empty_grid()
        self.view.show_payment_menu(paymentmethod.options)

    def cancelpay(self): self.toggle(); self.toggle()  # HACK: Double toggle to restart, pretty dirty fix

    def get_all_names_of(self, tablename):
        from importlib import import_module  # To be used to import the module corresponding to the given table name
        from inspect import getmembers, isclass  # To be used to fetch the relevant class within the imported module
        for classname, classref in getmembers(import_module('.' + tablename, "models")):
            if isclass(classref) and classname != "AbstractModel": return classref.get_all_names()

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


class ViewPrevDonations(AbstractToggleableController):
    def __init__(self, toggler): super().__init__(toggler=toggler)
    def start(self): self.view = placeholder.View(parentcontroller=self)


class ViewDonations(AbstractToggleableController):
    def __init__(self, toggler): super().__init__(toggler=toggler)
    def start(self): self.view = placeholder.View(parentcontroller=self)

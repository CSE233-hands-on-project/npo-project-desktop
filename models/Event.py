class Event:
    ID = 0
    def __init__(self, name, type, description, ocurrances):
        Event.ID += 1
        self.ID = Event.ID
        self.name = name
        self.type = type
        self.description = description
        self.ocurrances = ocurrances

    def change_name(self, new_name):
        self.name = new_name

    def change_type(self, new_type):
        self.type = new_type

    def change_Location(self, new_Location):
        self.Location = new_Location

class Registration:
    ID = 0
    def __init__(self, user_id, Location, date, time, All_Events):
        Registration.ID += 1
        self.ID = Registration.ID
        self.user_id = user_id
        self.Location = Location
        self.date = date
        self.time = time
        self.All_Events = All

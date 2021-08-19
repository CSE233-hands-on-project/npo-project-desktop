class RegistrationDetails:
    ID = 0
    def __init__(self, no_members, no_participations, Location, date, RegDetails):
        RegistrationDetails.ID += 1
        self.ID = RegistrationDetails.ID
        self.no_members = no_members
        self.Location = Location
        self.date = date
        self.RegDetails = RegDetails
        self.no_participations = no_participations
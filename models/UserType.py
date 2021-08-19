class UserType:
    ID = 0
    def __init__(self, type_name):
        UserType.ID += 1
        self.ID = UserType.ID
        self.name = type_name

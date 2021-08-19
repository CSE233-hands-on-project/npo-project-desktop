class User:
    ID = 0
    def __init__(self, name, address, age, national_id, Reg, UserType, role):
        User.ID += 1
        self.ID = User.ID
        self.name = name
        self.role = role
        self.address = address
        self.age = age
        self.national_id = national_id
        self.reg = Reg
        self.UserType = UserType

    def change_name(self, new_name):
        self.name = new_name

    def change_role(self, new_role):
        self.role = new_role

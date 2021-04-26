class Member():
    def __init__(self, first_name, last_name, email, premium, active=True, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.premium = premium
        self.active = active
        self.id = id

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
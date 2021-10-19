class Employee():
    def __init__(self, first_name, last_name, birth_day, sex, social_security_number, location):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_day = birth_day
        self.sex = sex
        self.social_security_number = social_security_number
        self.location = location

    @classmethod
    def from_input(cls):
        return cls(
        input("First name: ").capitalize(),
        input("Last name: ").capitalize(),
        input("Birth date (Year-Month-Day): "),
        input("Gender (F/M): ").upper(),
        input("Social security number: "),
        input("Location: ").capitalize()
        )




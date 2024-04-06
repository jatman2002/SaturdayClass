from datetime import date

class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob # as a date obj

    def get_current_age(self):
        today = date.today()
        number_of_days = (today - self.dob).days
        age = number_of_days // 365
        return age

    def print_message(self):
        return f'The person called {self.name} who lives in {self.country} was born on {self.dob} ' + \
            f'and is therefore {self.get_current_age()} years old.'

me = Person("Jatin", "UK", date(2002, 6, 27))
print('\n' + me.print_message() + '\n')
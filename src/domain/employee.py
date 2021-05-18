class Employee:
    def __init__(self, name,working_schedule):
        self.name = name
        self.working_schedule = working_schedule
        self.salary = 0.0

    
    def __str__(self):
        return  f'The amount to pay {self.name} is: {self.salary:.2f} USD'

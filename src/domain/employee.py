from src.service.input_parsing import get_working_shifts,get_working_shift_day_abbreviation,get_working_shift_times
from .shift import Shift
class Employee:
    def __init__(self, name,working_schedule):
        self.name = name
        self.working_schedule = working_schedule
        self.salary = 0.0

    def calculate_salary(self):
        calculated_salary = 0.0
        shifts = get_working_shifts(self.working_schedule)
        for shift in shifts:
            day_abbr = get_working_shift_day_abbreviation(shift)
            start,end = get_working_shift_times(shift)
            calculated_salary += Shift(day_abbr,start,end).get_shift_cost() 
        self.salary = calculated_salary   
        return calculated_salary

    def __str__(self):
        return  f'The amount to pay {self.name} is: {self.salary:.2f} USD'

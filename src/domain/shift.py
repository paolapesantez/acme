from src.service.hourly_payment import HourlyPayment
from src.service.abbreviations import WEEKEND
from src.service.time_handler import to_datetime_from_str, time_elapsed_in_hours, to_str_from_datetime,check_start_hour,check_end_hour
from datetime import timedelta

class Shift:
    
    def __init__(self,day_abbreviation,start_time,end_time):
        self.day = day_abbreviation
        self.start_time =  to_datetime_from_str(start_time)
        self.end_time =  to_datetime_from_str(end_time)
        self.__check_hours()

    def __check_hours(self):
        check_start_hour(self.start_time)
      
    def get_shift_cost(self):
        when = 'week'
        if self.day in WEEKEND:
            when = 'weekend'

        hourly_rates = HourlyPayment().get_hourly_rates()
        cost = 0.0
        different_hourly_rates = False
        worked_hours = 0.0
        minute = timedelta(minutes=1) 

        for value in hourly_rates.values():
            rate = value[when]
            rate_start_time = to_datetime_from_str(value['start_time'])
            rate_end_time = to_datetime_from_str(value['end_time'])
            
            #print(f'Rate end time: {rate_end_time}')
            end_of_day = check_end_hour(rate_end_time)
            if self.start_time >= rate_start_time and (self.start_time <= rate_end_time or end_of_day): 
                #Check whether all the worked hours belong to the same hourly rate
                if (self.end_time <= rate_end_time and not check_end_hour(self.end_time)) or end_of_day:
                    if different_hourly_rates:
                        self.start_time = self.start_time - minute
                        different_hourly_rates = False
                    if end_of_day and check_end_hour(self.end_time):    
                        worked_hours = 24-self.start_time.hour
                    else:
                        worked_hours = time_elapsed_in_hours(self.start_time,self.end_time)    
                    cost +=  worked_hours * rate
                    break
                  
                else: #when the shift has hours from different rates
                    if different_hourly_rates: #Adjust the cost that misses the one minute extra of starting a new hourly rate
                        self.start_time = self.start_time - minute
                    if end_of_day:    
                        worked_hours = 24-self.start_time.hour
                    else: 
                        worked_hours = time_elapsed_in_hours(self.start_time,rate_end_time)    
                    cost += worked_hours * rate
                    different_hourly_rates = True
                    self.start_time = rate_end_time + minute
      
        return cost
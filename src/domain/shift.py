class Shift:
    
    def __init__(self,day_abbreviation,start_time,end_time):
        self.day = day_abbreviation
        self.start_time =  start_time
        self.end_time =  end_time

    def get_shift_cost(self):
        return 0.0
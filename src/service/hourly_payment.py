class HourlyPayment:
    
    __hourly_rates = {
        'morning':{
            'start_time':'00:01',
            'end_time':'09:00',
            'week': 25,
            'weekend': 30
        },
        'afternoon':{
            'start_time':'09:01',
            'end_time':'18:00',
            'week': 15,
            'weekend': 20
        },
        'ninght':{
            'start_time':'18:01',
            'end_time':'00:00',
            'week': 20,
            'weekend': 25
        }
    }

    def get_hourly_rates(self):
        return self.__hourly_rates.copy()
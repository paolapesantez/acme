import unittest
from src.service import input_parsing

class TestInputParsing(unittest.TestCase):

    def test_get_employee_name(self):
        employee_text = 'RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00'

        name = input_parsing.get_employee_name(employee_text)

        self.assertEqual(name,'RENE')


    def test_get_employee_name_error(self):
        employee_text = 'RENEMO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00'

        with self.assertRaises(SystemExit) as ae:
            name = input_parsing.get_employee_name(employee_text)

        self.assertEqual(ae.exception.code,1)
        

    def test_get_employee_working_schedule(self):
        employee_text = 'RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00'

        working_schedule = input_parsing.get_employee_working_schedule(employee_text)

        self.assertEqual(working_schedule,'MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00')


    def test_get_employee_working_schedule_error(self):
        employee_text = 'RENEMO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00'

        with self.assertRaises(SystemExit) as ae:
            working_schedule = input_parsing.get_employee_working_schedule(employee_text)

        self.assertEqual(ae.exception.code,1)

    def test_get_working_shift_day_abbreviation(self):
        shift = 'MO10:00-12:00'

        day = input_parsing.get_working_shift_day_abbreviation(shift)

        self.assertEqual(day,'MO')

    def test_get_working_shift_day_abbreviation_error(self):
        shift = 'MU10:00-12:00'

        with self.assertRaises(SystemExit) as ae:
            day = input_parsing.get_working_shift_day_abbreviation(shift)

        self.assertEqual(ae.exception.code,1)    

    
    def test_get_working_shift_times(self):
        shift = 'MO10:00-12:00'

        start_time,end_time = input_parsing.get_working_shift_times(shift)

        self.assertEqual(start_time,'10:00')
        self.assertEqual(end_time,'12:00')    

    def test_get_working_shift_times_error1(self):
        shift = 'MO10:0012:00'

        with self.assertRaises(SystemExit) as ae:
            start_time,end_time = input_parsing.get_working_shift_times(shift)

        self.assertEqual(ae.exception.code,1)  


    def test_get_working_shift_times_error2(self):
        shift = 'MO10:00-1200'

        with self.assertRaises(SystemExit) as ae:
            start_time,end_time = input_parsing.get_working_shift_times(shift)

        self.assertEqual(ae.exception.code,1)  
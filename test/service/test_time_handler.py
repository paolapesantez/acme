import unittest 
from src.service.time_handler import time_elapsed_in_hours, to_datetime_from_str

class TestTimeHandler(unittest.TestCase):

    def test_to_datetime_from_str(self):
        time_str = '09:30'

        time_dt = to_datetime_from_str(time_str)

        self.assertEqual(time_dt.minute, 30)

    def test_calculate_elapsed_time_in_hours(self):
        start = to_datetime_from_str('11:25')
        end = to_datetime_from_str('12:55')

        time = time_elapsed_in_hours(start,end)

        self.assertEqual(time, 1.5)

    def test_calculate_elapsed_time_in_hours_error(self):
        start = to_datetime_from_str('13:25')
        end = to_datetime_from_str('12:55')

        with self.assertRaises(SystemExit) as ae:
            time = time_elapsed_in_hours(start,end)

        self.assertEqual(ae.exception.code, 1)    
    
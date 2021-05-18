import unittest
from src.domain.shift import Shift


class TestShift(unittest.TestCase):

    def test_get_shift_cost(self):
        shift = Shift('MO','10:00','12:00')

        cost = shift.get_shift_cost()

        self.assertEqual(cost,30)


    def test_get_shift_cost_error(self):
        shift = Shift('MO','12:00','10:00')

        with self.assertRaises(SystemExit) as ae:
            cost = shift.get_shift_cost()

        self.assertEqual(ae.exception.code,1)
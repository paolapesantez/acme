import unittest
from src.domain.employee import Employee

class TestEmployee(unittest.TestCase):

    def test_calculate_salary(self):
        employee = Employee('JOSEPH','MO10:00-12:00,TH12:00-14:00,SU20:00-21:00')
               
        # RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00
        # ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00  
        
        salary = employee.calculate_salary()
        print(employee)

        self.assertEqual(salary,85)

    def test_calculate_salary_error(self):
        employee = Employee('RENE','MO10:00-12:00,,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00')
                
        with self.assertRaises(SystemExit) as ae:
            employee.calculate_salary()

        self.assertEqual(ae.exception.code,1)
        

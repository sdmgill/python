import unittest
from employee import Employee

class TestEmployeeRaise(unittest.TestCase):
    """Test to see if raises work"""

    def setUp(self):
        """ Create test employee to use in multiple test"""
        self.my_employee = Employee('sean', 'gill', 100000)

    def test_default_raise(self):
        """Test default raise"""
        self.my_employee.give_raise()
        #self.my_employee.show_employee_info()
        self.assertEqual(self.my_employee.salary,105000)

    def test_custom_raise(self):
        """Test custom raise"""
        self.my_employee.give_raise(25000)
        #self.my_employee.show_employee_info()
        self.assertEqual(self.my_employee.salary, 125000)

if __name__ == '__main__': # needed to add this part since the code kept failing. Researched online.
    unittest.main()
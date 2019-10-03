import unittest
from city_function import get_city_country

class CityTestCase(unittest.TestCase):
    """Verify that city_function.py is working properly"""
    def test_city_country(self):
        """Do cities like Toronto, Canada work"""
        formatted_city = get_city_country('toronto', 'canada', 50000)
        self.assertEqual(formatted_city, 'Toronto, Canada - Population 50000')

if __name__ == '__main__': # needed to add this part since the code kept failing. Researched online.
    unittest.main()
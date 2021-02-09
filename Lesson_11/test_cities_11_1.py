import unittest
from city_functions_11_1 import city_country


class TestCityFunctions(unittest.TestCase):

    def test_city_country(self):
        formatted_name = city_country('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago Chile')


if __name__ == '__main__':
    unittest.main()

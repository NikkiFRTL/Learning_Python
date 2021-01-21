import unittest
from Lesson_11.city_functions import city_country


class TestCityFunctions(unittest.TestCase):

    def test_city_country(self):
        formatted_name = city_country('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago Chile')


if __name__ == '__main__':
    unittest.main()

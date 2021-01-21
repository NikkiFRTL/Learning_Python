import unittest
from Lesson_11.population_11_2 import city_country


class TestCityFunctions(unittest.TestCase):

    def test_city_country(self):
        formatted_name = city_country('santiago', 'chile', population='5000000')
        self.assertEqual(formatted_name, 'Santiago Chile - Population 5000000')


if __name__ == '__main__':
    unittest.main()

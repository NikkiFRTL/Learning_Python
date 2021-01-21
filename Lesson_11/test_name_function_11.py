import unittest
from Lesson_11.name_function.format_name import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """
    Tests correctness of get_formatted_name method
    """
    def test_first_last_name(self):
        formatted_name = get_formatted_name('joe', 'biden')
        self.assertEqual(formatted_name, 'Joe Biden')


if __name__ == '__main__':
    unittest.main()

import unittest
from Lesson_11.employee_11_3 import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.worker = Employee('Nick', 'Ch', 90000)

    def test_give_default_raise(self):
        self.worker.get_raise()
        self.assertEqual(self.worker.salary, 95000)

    def test_give_custom_raise(self):
        self.worker.get_raise(20000)
        self.assertEqual(self.worker.salary, 110000)


if __name__ == "__main__":
    unittest.main()

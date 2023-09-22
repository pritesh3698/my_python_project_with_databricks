import unittest
from my_module.simple_math import add_numbers

class TestSimpleMath(unittest.TestCase):

    def test_addition(self):
        result = add_numbers(2, 3)
        self.assertEqual(result, 5)

    def test_negative_numbers(self):
        result = add_numbers(-2, 3)
        self.assertEqual(result, 1)

    def test_decimal_numbers(self):
        result = add_numbers(1.5, 2.5)
        self.assertEqual(result, 4.0)

if __name__ == '__main__':
    unittest.main()

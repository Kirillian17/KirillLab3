# test_even_odd_checker.py
import unittest
from even_odd_checker import check_even_odd

class TestEvenOddChecker(unittest.TestCase):
    def test_even_number(self):
        result = check_even_odd(4)
        self.assertEqual(result, "Парне число")

    def test_odd_number(self):
        result = check_even_odd(7)
        self.assertEqual(result, "Непарне число")

if __name__ == "__main__":
    unittest.main()

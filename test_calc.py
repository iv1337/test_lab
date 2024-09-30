import unittest
from calc import add, subtract, multiply, divide 
 
class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 3), 8)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(multiply(2, 4), 8)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        self.assertEqual(divide(10, 0), "divide on zero!")

if __name__ == '__main__':
    unittest.main()

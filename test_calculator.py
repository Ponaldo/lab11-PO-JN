# https://github.com/Ponaldo/lab11-PO-JN
# Partner 1: Purab Ojha
# Partner 2: José Borges da Cruz Neto
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(2, 2), 4)
        self.assertEqual(add(3, 4), 7)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(4, 2), 2)
        self.assertEqual(subtract(2, 2), 0)
        self.assertEqual(subtract(0, 0), 0)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-2, 5), -10)
        self.assertEqual(mul(7, 0), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(2, 10), 5)
        self.assertEqual(div(-2, 10), -5)
        self.assertAlmostEqual(div(4, 2), 0.5)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(10, 100), 2)
        self.assertAlmostEqual(logarithm(5, 1), 0)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(-2, 8)
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(2, 0)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(-3, -4), 5)
        self.assertAlmostEqual(hypotenuse(1, 1), 1.41421356, places=6)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertEqual(square_root(16), 4)
        self.assertAlmostEqual(square_root(2), 1.41421356, places=6)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
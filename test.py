#!/usb/bin/env python

import maths
import unittest

class TestSum(unittest.TestCase):
    """
    Test the addition function
    """
    def test_sum_integers(self):
        """
        Test the addition of integers
        """
        result = maths.addition(3,5)
        self.assertEqual(result, 8)

    def test_sum_floats(self):
        """
        Test the addition of floats
        """
        result = maths.addition(15.3,27.8)
        self.assertEqual(result, 43.1)

class TestSubs(unittest.TestCase):
    """
    Test the subtraction function
    """

    def test_subtract_integers(self):
        result = maths.subtract(15,7)
        self.assertEqual(result,8)

class TestMultiply(unittest.TestCase):
    """
    Test the multiplication function
    """

    def test_multiply_integers(self):
        result = maths.multiply(8,7)
        self.assertEqual(result,56)

class TestDivision(unittest.TestCase):
    """
    Test the division function
    """

    def test_division_integers(self):
        result = maths.divide(20,8)
        self.assertEqual(result,2.5)

if __name__ == '__main__':
    unittest.main()
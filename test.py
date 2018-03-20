#!/usb/bin/env python

import maths
import unittest

class TestSum(unittest.TestCase):
    """
    Test the sum function
    """
    def test_sum_integers(self):
        """
        Test the sum of integers
        """
        result = maths.sum(3,5)
        self.assertEqual(result, 8)

    def test_sum_floats(self):
        """
        Test the sum of floats
        """
        result = maths.sum(15.3,27.8)
        self.assertEqual(43.1)

if __name__ == '__main__':
    unittest.main()
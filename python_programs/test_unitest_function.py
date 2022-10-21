#!/usr/bin/python3
# unittests for unitest_function.py

import unittest
from unitest_function import add, sub, mul, div, mod

class TestUnitest_Function(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 1), 2)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(-1.5, -1.4), -2.9)

    def test_sub(self):
        self.assertEqual(sub(1, 1), 0)
        self.assertEqual(sub(-1, 1), -2)
        self.assertEqual(sub(-1, -1), 0)
        self.assertAlmostEqual(sub(-1.5, -1.4), -0.1)

    def test_mul(self):
        self.assertEqual(mul(1, 1), 1)
        self.assertEqual(mul(-1, 1), -1)
        self.assertEqual(mul(-1, -1), 1)
        self.assertAlmostEqual(mul(-1.5, -1.4), 2.0999999999999996)

    def test_div(self):
        self.assertEqual(div(4, 2), 2)
        self.assertEqual(div(-6, 3), -2)
        self.assertEqual(div(-1, -1), 1)
        self.assertAlmostEqual(div(-1.5, -1.4), 1.0714285714)
    '''
    def test_add(self):
        self.assertEqual(add(1, 1), 2)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(-1.5, -1.4), -2.9)
    '''

if __name__ == "__main__":
    unittest.main()


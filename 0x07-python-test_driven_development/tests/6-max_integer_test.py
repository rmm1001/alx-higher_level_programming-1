import unittest
""" This module tests the max_integer module
"""


from ..max_integer import max_integer

class MaxIntegerTest(unittest.TestCase):
    def test_max_at_the_end(self):
        self.assertEqual(max_integer([1,2,3]), 3)

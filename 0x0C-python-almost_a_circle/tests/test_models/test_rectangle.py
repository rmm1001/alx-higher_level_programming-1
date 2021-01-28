#!/usr/bin/python3
"""Unittests for base
"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Define unit test for Rectangle model"""

    def test_initialization(self):
        r1 = Rectangle(2,5)
        r2 = Rectangle(1,2)
        self.assertEqual(r1.id, 3)
        self.assertEqual(r2.id, 4)


if __name__ == '__main__':
    unittest.main()

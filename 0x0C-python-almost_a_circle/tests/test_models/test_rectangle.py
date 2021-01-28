#!/usr/bin/python3
"""Unittests for base
"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Define unit test for Rectangle model"""

    def test_initialization(self):
        r1 = Rectangle()
        r2 = Rectangle()
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)


if __name__ == '__main__':
    unittest.main()

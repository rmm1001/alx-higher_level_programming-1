#!/usr/bin/python3
"""Unittests for base
"""

import unittest
from models.square import Square


class TestRectangle(unittest.TestCase):
    """Define unit test for Square model"""

    def test_initialization(self):
        s1 = Square()
        s2 = Square()
        self.assertEqual(s1.id, 1)
        self.assertEqual(s2.id, 2)


if __name__ == '__main__':
    unittest.main()

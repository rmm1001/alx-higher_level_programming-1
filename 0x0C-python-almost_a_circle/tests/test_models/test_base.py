#!/usr/bin/python3
"""Unittests for base
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Define unit test for Base model"""

    def test_initialization(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)


if __name__ == '__main__':
    unittest.main()

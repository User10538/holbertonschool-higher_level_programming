#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_unordered_list(self):
        self.assertEqual(max_integer([3, 2, 1, 4]),4)

    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]),4)

    def test_max_start(self):
        self.assertEqual(max_integer([8, 2, 0, 4]),8)

    def test_max_middle(self):
        self.assertEqual(max_integer([8, 9, 1]),9)

    

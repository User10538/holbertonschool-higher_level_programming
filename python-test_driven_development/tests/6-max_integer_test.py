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

    def test_negative_number(self):
        self.assertEqual(max_integer([8, -9, 1]),8)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-8, -9, -15]),-15)

    def test_one_element(self):
        self.assertEqual(max_integer([8]),8)

    def test_empty(self):
        self.assertEqual(max_integer([]))

    

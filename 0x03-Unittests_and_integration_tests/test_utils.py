#!/usr/bin/env python3
""" Parameterize a unit test """

from parameterized import parameterized
import unittest
from unittest.mock import patch
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ TestAccessNestedMap cllas"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test test_access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path, expected))

    @parameterized.expand([
        ({}, ("a"), ),
        ({"a": 1}, ("a", "b"), ),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ Test test_access_nested_map_exception function"""
        with self.assertRaises(KeyError) as cont:
            access_nested_map(nested_map, path)
        self.assertEqual(type(cont.exception), KeyError)

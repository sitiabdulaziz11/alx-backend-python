#!/usr/bin/env python3
""" Parameterize a unit test """

from parameterized import parameterized
import unittest
from unittest.mock import patch
from utils import (access_nested_map, get_json, memoize)
import unittest.mock as Mock
import requests


class TestAccessNestedMap(unittest.TestCase):
    """ TestAccessNestedMap cllas"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test test_access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a"), ),
        ({"a": 1}, ("a", "b"), ),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ Test test_access_nested_map_exception function"""
        with self.assertRaises(KeyError) as cont:
            access_nested_map(nested_map, path)
        self.assertEqual(type(cont.exception), KeyError)


class TestGetJson(unittest.TestCase):
    @patch('utils.requests.get')
    def test_get_json(self, mock_get):
        test_cases = [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]

        for test_url, test_payload in test_cases:
            # Mocking the response from requests.get
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response
            result = get_json(test_url)
            # Call the get_json function with the test URL
            mock_get.assert_called_once_with(test_url)
            # Assertions
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """ TestMemoize class """

    def test_memoize(self):
        """ Test test_memoize function"""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass,
                          'a_method', return_value=42) as mock_method:
            test_class = TestClass()
            self.assertEqual(test_class.a_property, 42)
            self.assertEqual(test_class.a_property, 42)
            mock_method.assert_called_once()

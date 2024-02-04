#!/usr/bin/env python3
"""Module for testing utils.access_nested_map"""
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, Mock
from utils import *


class TestAccessNestedMap(unittest.TestCase):
    """Tests for utils.access_nested_map"""

    nested_map1 = {"a": 1}
    path1 = ("a",)
    nested_map2 = {"a": {"b": 2}}
    path2 = ("a",)
    nested_map3 = {"a": {"b": 2}}
    path3 = ("a", "b")

    @parameterized.expand([
        (nested_map1, path1, 1),
        (nested_map2, path2, {"b": 2}),
        (nested_map3, path3, 2),
        ])
    def test_access_nested_map(self, nested_map, path, expected):
        """test for utils.access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
        ])
    def test_access_nested_map_exception(self, nested_map, path):
        """test for keyError exception"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """test for get_json"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        # Set up the mock response and attach it to the get method
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Call the get_json function
        result = get_json(test_url)

        # Assert that the get method was called exactly once with the URL
        mock_get.assert_called_once_with(test_url)

        # Assert that the output of get_json is equal to test_payload
        self.assertEqual(result, test_payload)


if __name__ == '__main__':
    unittest.main()

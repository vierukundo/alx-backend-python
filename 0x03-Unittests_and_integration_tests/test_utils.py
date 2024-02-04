#!/usr/bin/env python3
"""Module for testing utils.access_nested_map"""
import unittest
from parameterized import parameterized, parameterized_class
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

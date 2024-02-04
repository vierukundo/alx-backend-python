#!/usr/bin/env python3
"""Module with tests for client"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Representation of class for testing client"""

    @parameterized.expand(["google", "abc"])
    @patch("client.get_json")
    def test_org(self, org, mock_get_json):
        """Test for org method"""
        test_instance = GithubOrgClient(org)

        test_instance.org
        url = test_instance.ORG_URL.format(org=org)
        mock_get_json.assert_called_once_with(url)


if __name__ == "__main__":
    unittest.main()

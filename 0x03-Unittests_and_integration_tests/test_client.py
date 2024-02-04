#!/usr/bin/env python3
"""Module with tests for client"""
import unittest
from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import patch, Mock, MagicMock, PropertyMock


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

    @patch('client.GithubOrgClient.org', return_value={"repos_url": 'url'})
    def test_public_repos_url(self, mocked_org):
        """Test the _public_repos_url property of GithubOrgClient."""
        inst = GithubOrgClient('random org url')
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mocked_property:
            mocked_property.return_value = mocked_org.return_value["repos_url"]
            repo_url = inst._public_repos_url
        self.assertEqual('url', repo_url)


if __name__ == "__main__":
    unittest.main()

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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test for public_repos method"""

        # Mock the return value of get_json
        repos_payload = [
            {"name": "vierukundo"},
            {"name": "rukundo"},
            {"name": "sam"}
        ]
        mock_get_json.return_value = repos_payload

        # Mock the _public_repos_url property
        repos_url = "https://github.com/repos"
        with patch(
                'client.GithubOrgClient._public_repos_url',
                new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = repos_url

            # Create an instance of GithubOrgClient
            instance = GithubOrgClient("org")

            # Call the public_repos method
            list_of_repos = instance.public_repos()

        # Assert that the result matches the expected list
        self.assertEqual(list_of_repos, ["vierukundo", "rukundo", "sam"])

        # Assert that the get_json and _public_repos_url were called once
        mock_get_json.assert_called_once_with(repos_url)
        mock_public_repos_url.assert_called_once()


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
"""
Takes Github credentials and uses the GitHub API to display id
Uses Basic Authentication with a PAT as password to access info
"""

import sys
import requests


def get_github_userid(username, token):
    url = "https://api.github.com/user"
    auth = (username, token)
    response = requests.get(url, auth=auth)
    if response.status_code == 200:
        data = response.json()
        print(data['id'])
    else:
        print("None")


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    get_github_userid(username, token)

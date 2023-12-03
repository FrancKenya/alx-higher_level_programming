#!/usr/bin/python3
"""
Lists 10 last commits by a user of a repo 'rails' by a user using github API
"""
import sys
import requests


def commits_lists(repo, owner):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    params = {'author': owner, 'page': 10}

    response = requests.get(url, params=params)
    if response.status_code == 200:
        commits = response.json()
        for i in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
        else:
            print(response.status_code)


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    commits_lists(repo, owner)

#!/usr/bin/python3
"""
Scripts send a request to a url and displays the value of the variable
X-Request-Id in the response header.
Only import requests and sys packages
"""
import sys
import requests


def request_id(url):
    response = requests.get(url)
    x_request_id = response.headers.get('X-Request-Id')
    print(x_request_id)


if __name__ == "__main__":
    url = sys.argv[1]
    request_id(url)

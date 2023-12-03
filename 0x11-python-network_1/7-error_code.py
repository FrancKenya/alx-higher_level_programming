#!/usr/bin/python3
"""
A script that uses requests to send request to the URL.
Displays the body of the response.
Displays error code if HTTP status code is greater than
or equal to 400
"""
import sys
import requests


def handle_error(url):
    response = requests.get(url)
    if response.status_code < 400:
        print(response.text)
    else:
        print(f"Error code: {response.status_code}")


if __name__ == "__main__":
    url = sys.argv[1]
    handle_error(url)

#!/usr/bin/python3
"""
A script that takes a URL and email address, sends a POST request to
the URL with the email as parameter and finally displays the body of the
response
Only use sys and requests package
"""
import sys
import requests


def post_request(url, email):
    data = {'email': email}
    response = requests.post(url, data)
    print(response.text)


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    post_request(url, email)

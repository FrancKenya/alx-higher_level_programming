#!/usr/bin/python3
"""
A script that takes in a URL, email and sends POST request to the passed
URL with the email as parameter and displays the body of the response
decoded in utf-8
"""
import urllib.parse
import urllib.request
import sys


def post_request(url, email):
    data = urllib.parse.urlencode(email)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')

    with urllib.request.urlopen(req) as response:
        undecoded_body = response.read()
        body = undecoded_body.decode('utf-8')
        print(body)


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    post_request(url, email)

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
    # use parse.urlencode to encode the argument
    data = urllib.parse.urlencode({'email': email})
    # convert it in to bytes
    data = data.encode('ascii')
    # make an object request
    req = urllib.request.Request(url, data)

# Use with to open url response and decode
    with urllib.request.urlopen(req) as response:
        undecoded_body = response.read()
        body = undecoded_body.decode('utf-8')
        print(body)


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    post_request(url, email)

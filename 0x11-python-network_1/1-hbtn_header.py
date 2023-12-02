#!/usr/bin/python3
"""
Script takes a URL takes a request to the URL and displays the value of
the request id variable found in the header
"""
import urllib.request
import sys


def get_url_id(url):
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:

        # use .headers.get get to get the id  of HTTP header
        request_id = response.headers.get('X-Request-Id')
        print(request_id)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    url = sys.argv[1]
    get_url_id(url)

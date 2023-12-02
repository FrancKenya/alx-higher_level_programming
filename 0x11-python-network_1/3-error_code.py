#!/usr/bin/python3
"""
A script that sends a request to the URL and displays the body
of the response
Also manages urllib.error.HTTPError exceptions and print Error code followed
by HTTP status
Must use with statement
"""
import urllib.request
import sys
import urllib.error


def handle_http_error(url):
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            body = response.read()
            dec_body = body.decode('utf-8')
            print(body)
    except urllib.error.HTTPError as err:
        print("Error code:", err.code)


if __name__ == "__main__":
    url = sys.argv[1]
    handle_http_error(url)

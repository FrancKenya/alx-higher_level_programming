#!/usr/bin/python3
"""
A python script that fetches a url using urllib
Not allowed to import any packages apart from urllib
"""

import urllib.request


def get_status():
    url = 'https://alx-intranet.hbtn.io/status'
    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        body = response.read()
        content_decode = body.decode('utf-8')
        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body)
        print("\t- utf8 content:", content_decode)


if __name__ == "__main__":
    get_status()

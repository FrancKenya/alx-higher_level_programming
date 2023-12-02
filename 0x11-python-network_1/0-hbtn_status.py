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
        the_page = response.read
        content_decode = the_page.decode('utf-8')
        print("Body response:")
        print("\t- type:", type(the_page))
        print("\t- content:", the_page)
        print("\t- utf8 content:", content_decode)


if __name__ == "__main__":
    get_status()

#!/usr/bin/python3
"""
This script fetches the given url and and displays the body of the response
Only allowed to import requests
"""
import urllib.request


def fetch_url():
    url = "https://alx-intranet.hbtn.io/status"
    # make an object
    req = urllib.request.Request(url)
    # use with to make the request and close
    with urllib.request.urlopen(req) as response:
        data = response.read()
        body = data.decode('utf-8')
        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body)


if __name__ == "__main__":
    fetch_url()

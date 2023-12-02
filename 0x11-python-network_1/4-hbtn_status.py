#!/usr/bin/python3
"""
This script fetches the given url and and displays the body of the response
Only allowed to import requests
"""
import requests


def fetch_url():
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.text.encode('utf-8')
        dec_data = data.decode('utf-8')
        print("Body response:")
        print("\t- type:", type(dec_data))
        print("\t- content:", dec_data)


if __name__ == "__main__":
    fetch_url()

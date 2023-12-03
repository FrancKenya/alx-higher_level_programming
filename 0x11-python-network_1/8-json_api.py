#!/usr/bin/python3
"""
A scripts that takes a letter and sends a post request to a URL
with the letter as parameter
Letter must be sent in variable q
Handle no argument
"""
import sys
import requests


def search_by_letter(letter):
    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': letter}
    response = requests.post(url, data)
    json_response = response.json()
    if json_response:
        print("[{}] {}".format(json_response.get(
            'id'), json_response.get('name')))
    else:
        print("No result")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""
    search_by_letter(letter)

#!/bin/bash
# This script takes in A URL, sends a request to that URL, and displays the size of the body of the response

url=$1

curl -s -o /dev/null -w "%{size_download}" "$url"

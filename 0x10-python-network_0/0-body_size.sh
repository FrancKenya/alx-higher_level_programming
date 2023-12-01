#!/bin/bash
# A script that sends a request to a URL, and displays the size of the body
if [ $# -ne 1 ]; then
	exit 1
fi
url=$1

curl -s -o /dev/null -w "%{size_download}" "$url"

#!/bin/bash
# A script that sends a request to a URL, and displays the size of the body
echo "$(curl -s -o /dev/null -w "%{size_download}\n" "$1")"

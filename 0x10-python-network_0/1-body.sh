#!/bin/bash
# Takes in a URL and sends a GET request and displays the body of the response
curl -s -X GET -o /dev/null -L "$1"


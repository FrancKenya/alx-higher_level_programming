#!/usr/bin/bash
# Sends DELETE request to URL passed as first argument and displays response body
curl -s -X DELETE "$1"

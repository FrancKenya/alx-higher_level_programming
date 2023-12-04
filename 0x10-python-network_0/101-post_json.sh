#!/bin/bash
# Sends a JSON POST request to a URL passed and displays response body
curl -s -X POST -H "Content-Type: application/json" -d "@$2" "$1"

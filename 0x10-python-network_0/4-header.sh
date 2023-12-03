#!/bin/bash
# Sends GET request and displays response body sending a header variable with the value 98
curl -s -H "X-School-User-Id: 98" "$1"

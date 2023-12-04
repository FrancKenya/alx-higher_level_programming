#!/bin/bash
# makes a URL request and gets a string response in the body
curl -s -X PUT -L -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me

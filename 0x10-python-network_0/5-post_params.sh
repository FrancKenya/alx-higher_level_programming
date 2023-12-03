#!/bin/bash
# Sends POST, display response body, email and subject variables sent
curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"

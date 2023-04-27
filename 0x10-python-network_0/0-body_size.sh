#!/usr/bin/env bash
# A Bash script that takes in a URL, sends a request to that URL \
#and displays the size of the body of the response

size=$(curl -s "$1" | tr -d '\r' | wc -c)
echo "$size"
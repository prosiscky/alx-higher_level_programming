#!/bin/bash
# Get the byte size of the HTTP response header for a given URL
url1=$url
curl -s "$url" | wc -c

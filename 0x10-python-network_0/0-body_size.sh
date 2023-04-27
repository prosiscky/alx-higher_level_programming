#!/bin/bash
# Get the byte size of the HTTP response header for a given URL

size=$(curl -s "$1" | tr -d '\r' | wc -c)
echo "$size"

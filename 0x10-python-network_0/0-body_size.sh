#!/bin/bash
# Get the byte size of the HTTP response header for a given URL.
curl -s "$url" | wc -c

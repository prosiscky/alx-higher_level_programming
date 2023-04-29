#!/usr/bin/python3


"""
 A Python script that takes in a URL,
sends a request to the URL and displays
the body of the response (decoded in utf-8).
REQUIREMENTS:
You have to manage urllib.error.HTTPError exceptions and print:
Error code: followed by the HTTP status code
You must use the packages urllib and sys
You are not allowed to import other packages than urllib and sys
You must use the with statement

"""


import urllib.request
import urllib.error
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")


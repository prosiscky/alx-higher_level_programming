#!/usr/bin/python3


"""
Python script that takes in a URL,
sends a request to the URL and
displays the value of the X-Request-Id variable found
in the header of the response.

REQUIREMENTS
You must use the packages urllib and sys
You are not allow to import packages other than urllib and sys
The value of this variable is different for each request
You don’t need to check arguments passed to the script (number or type)
You must use a with statement
"""

import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        header = response.info()
        x_request_id = header['X-Request-Id']
        print(x_request_id)
